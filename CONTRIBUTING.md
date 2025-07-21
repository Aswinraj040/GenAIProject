# 🤝 Contributing to GenSQL

Thank you for considering contributing to **GenSQL**! Your help is greatly appreciated. Whether you're fixing bugs, improving documentation, or suggesting new features—every bit helps.

---

## 📋 Table of Contents

- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)
- [Code Style Guide](#code-style-guide)
- [Reporting Bugs](#reporting-bugs)
- [Feature Requests](#feature-requests)
- [Pull Request Process](#pull-request-process)

---

## 🛠️ Getting Started

1. **Fork the repository**  
2. **Clone your fork**

   ```bash
   git clone https://github.com/Aswinraj040/GenSQL
   cd GenSql
```

3. **Set up the virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate       # macOS/Linux
   venv\Scripts\activate.bat      # Windows
   ```

4. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

5. **Create a `.env` file**

   ```
   GEMINI_API_KEY=your_gemini_api_key
   ```

6. **Run the server**

   ```bash
   uvicorn main:app --reload
   ```

---

## ✨ How to Contribute

* 🐛 **Fix bugs**
* 📚 **Improve documentation**
* 💡 **Suggest enhancements**
* 🧪 **Add test cases**
* 🌍 **Improve UI/UX in the frontend**
* 📤 **Optimize API calls or performance**

---

## 🧹 Code Style Guide

* Follow **PEP8** for Python code.
* Use **meaningful commit messages**.
* Keep pull requests **focused** and **descriptive**.
* Frontend should use clean HTML/CSS/JS structure (or React conventions if applicable).

---

## 🐞 Reporting Bugs

If you find a bug, please open an issue with the following details:

* ✅ Clear title and description
* 🧪 Steps to reproduce
* 📸 Screenshots/logs if applicable
* 💻 Your OS and Python version

---

## 🚀 Feature Requests

We love ideas! Please submit a feature request issue describing:

* What problem it solves
* What your idea does
* Optional: proposed code snippet or UI mockup

---

## 🔁 Pull Request Process

1. Create a feature branch

   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes

3. Commit clearly

   ```bash
   git commit -m "Add: descriptive message about your change"
   ```

4. Push to your fork

   ```bash
   git push origin feature/your-feature-name
   ```

5. Open a Pull Request on the original repository

---

## ❤️ Code of Conduct

Please be respectful and inclusive in all interactions. For full guidelines, refer to the [CODE\_OF\_CONDUCT.md](./CODE_OF_CONDUCT.md) file.

---

Happy coding! 🧠💻✨
— *GenSQL Maintainers*
