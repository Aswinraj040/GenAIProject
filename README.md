# 🔍 GenAI-Powered Natural Language to SQL App

This is a full-stack Python-based application that converts **natural language queries** into **SQL statements** using **Google's Gemini API**, executes them on a local **SQLite database**, and displays the results.

> 💡 Built with **FastAPI** for backend and vanilla HTML/CSS/JS for frontend.

---

## 🚀 Features

- Convert natural language to SQL using GenAI (Gemini).
- Execute real-time SQL queries on a pre-populated SQLite database.
- Clean, simple frontend for query input and result display.
- CORS enabled for easy local frontend-backend interaction.

---

## 📁 Project Structure

```

project-folder/
│
├── main.py                  # FastAPI backend server
├── requirements.txt         # Python dependencies
├── ServerDatabase.db        # SQLite3 database file
├── .env                     # Contains your Gemini API key (not committed)
├── README.md                # You're reading this!
│
└── frontend/
├── index.html           # Frontend UI
└── assets/              # Static assets (CSS/JS)

````

---

## 🧠 Powered by Gemini API

This project uses **Google's Gemini 1.5 Flash model** via the `google-generativeai` Python SDK to intelligently convert natural language queries into SQL.

---


## 🗂 Database Schema (ER Diagram)

<details> <summary>📊 Click to expand Mermaid Diagram</summary>
```mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```
</details>


## 🔧 Setup Instructions

### 1. 🧬 Clone the Repository

```bash
git clone https://github.com/Aswinraj040/GenSQL
cd GenSQL
````

---

### 2. 🧪 Set Up Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate it (Windows)
venv\Scripts\activate

# OR (macOS/Linux)
source venv/bin/activate
```

---

### 3. 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. 🔐 Set Up Gemini API Key

1. Go to [https://makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)
2. Generate your Gemini API key
3. Create a `.env` file in the root of your project and paste:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

✅ Make sure the `.env` file is **not committed** to GitHub.

---

### 5. 🧠 Run the Backend Server

```bash
uvicorn main:app --reload
```

> 📍 Server will start at `http://127.0.0.1:8000`

---

### 6. 💻 Open the Frontend

Open the file directly in your browser:

```bash
frontend/index.html
```

Or better, use a local static server (recommended):

```bash
# If you have Python installed
cd frontend
python -m http.server 5500
```

Visit `http://localhost:5500` in your browser.

---

## ⚙️ How It Works

* User types a query like:
  **"Show me all books sold after July 1st with quantity more than 3"**
* The backend sends the query to Gemini.
* Gemini returns a valid SQL query.
* The backend runs it on `ServerDatabase.db`.
* The results are returned and displayed in the frontend.

---

## ✅ Example Natural Language Queries

* "List all books by authors from the UK"
* "What is the total sales quantity for each book?"
* "Which books have genre 'Horror' and price below 10?"

---

## 🔐 Security Notes

* This app uses `sqlite3`, which is safe for small-scale apps but should not be used in production for multi-user systems.
* Input sanitization is not necessary here due to LLM-generated SQL, but you should **never expose raw SQL execution in production**.
* Always keep your `.env` secrets out of version control.

---

## 📜 License

MIT License — feel free to use, improve, and contribute!

---

## 🙋 Support

If you find this project helpful, give it a ⭐ on GitHub and consider sharing it.
Have issues or ideas? Open an [Issue](https://github.com/your-username/genai-sql-assistant/issues) or [Pull Request](https://github.com/your-username/genai-sql-assistant/pulls)!

---

Made with ❤️ using FastAPI, Gemini, and SQLite.
