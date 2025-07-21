from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
import os
from dotenv import load_dotenv
import google.generativeai as genai
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS (allow all origins for development)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to specific origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


load_dotenv()


# Gemini Setup
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

DATABASE = "ServerDatabase.db"

class NLQuery(BaseModel):
    query: str

class SQLQuery(BaseModel):
    sql: str

# === 1. CREATE SCHEMA AND INSERT SAMPLE DATA ===
def initialize_database():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.executescript("""
    DROP TABLE IF EXISTS Sales;
    DROP TABLE IF EXISTS Books;
    DROP TABLE IF EXISTS Authors;

    CREATE TABLE Authors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        country TEXT
    );

    CREATE TABLE Books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        genre TEXT,
        author_id INTEGER,
        price REAL,
        FOREIGN KEY (author_id) REFERENCES Authors(id)
    );

    CREATE TABLE Sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        book_id INTEGER,
        sale_date TEXT,
        quantity INTEGER,
        FOREIGN KEY (book_id) REFERENCES Books(id)
    );
    """)

    cursor.executemany("INSERT INTO Authors (name, country) VALUES (?, ?);", [
        ('George Orwell', 'UK'), ('Haruki Murakami', 'Japan'),
        ('J.K. Rowling', 'UK'), ('Stephen King', 'USA'),
        ('Chimamanda Ngozi Adichie', 'Nigeria')
    ])

    cursor.executemany("INSERT INTO Books (title, genre, author_id, price) VALUES (?, ?, ?, ?);", [
        ('1984', 'Dystopian', 1, 9.99),
        ('Kafka on the Shore', 'Magical Realism', 2, 12.50),
        ('Harry Potter', 'Fantasy', 3, 8.99),
        ('The Shining', 'Horror', 4, 10.00),
        ('Half of a Yellow Sun', 'Historical', 5, 11.25)
    ])

    cursor.executemany("INSERT INTO Sales (book_id, sale_date, quantity) VALUES (?, ?, ?);", [
        (1, '2025-07-01', 5), (2, '2025-07-02', 3), (3, '2025-07-03', 10),
        (4, '2025-07-04', 2), (5, '2025-07-05', 4)
    ])

    conn.commit()
    conn.close()

initialize_database()

# === 2. GENERATE SQL WITH GEMINI ===
def generate_sql_from_nl(query: str) -> str:
    model = genai.GenerativeModel("gemini-1.5-flash")  # You can also use "gemini-pro" or "gemini-1.0-pro"

    prompt = f"""
You are a professional data assistant. Convert the following natural language question to an accurate SQL query based on this schema:

Tables:
Authors(id, name, country)
Books(id, title, genre, author_id, price)
Sales(id, book_id, sale_date, quantity)

Return only the SQL query.

Question: {query}
"""

    print("==== Prompt Sent to Gemini ====")
    print(prompt)

    try:
        response = model.generate_content(prompt)
        # print the full response for inspection
        print("==== Raw Gemini Response ====")
        print(response)

        # This is a safer way to extract SQL from the response
        content = response.text.strip() if hasattr(response, 'text') else ""
        if not content and hasattr(response, 'parts'):
            content = "\n".join([part.text for part in response.parts if hasattr(part, "text")])

        print("==== Gemini Response Content ====")
        print(content)

        # Try to extract SQL block
        if "```sql" in content:
            content = content.split("```sql")[1].split("```")[0].strip()
        elif "```" in content:
            content = content.split("```")[1].split("```")[0].strip()

        return content.strip()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Gemini Error: {str(e)}")

# === 3. EXECUTE SQL ===
def execute_sql(sql: str):
    try:
        print("==== Executing SQL ====")
        print(sql)
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute(sql)
        columns = [desc[0] for desc in cursor.description] if cursor.description else []
        rows = cursor.fetchall()
        conn.close()
        return [dict(zip(columns, row)) for row in rows]
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"SQL Error: {str(e)}")

# === 4. API ROUTES ===
@app.post("/generate-sql")
def generate_sql(nl_query: NLQuery):
    sql = generate_sql_from_nl(nl_query.query)
    return {"sql": sql}

@app.post("/execute-sql")
def run_sql(sql_query: SQLQuery):
    result = execute_sql(sql_query.sql)
    return {"result": result}

@app.post("/query")
def full_query(nl_query: NLQuery):
    sql = generate_sql_from_nl(nl_query.query)
    result = execute_sql(sql)
    return {"sql": sql, "result": result}
