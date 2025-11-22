
---

# 🏥 Triage Recommendation API

### FastAPI + Google Gemini + LangChain

A lightweight **AI-powered hospital triage recommendation service**.
Given patient info (gender, age, symptoms), the API uses **Google Gemini (via LangChain)** to automatically recommend the most relevant medical department.

---

## 🚀 Features

* FastAPI backend
* Google Gemini 2.0 Flash (LangChain wrapper)
* Clean triage prompt for medical routing
* Simple structure, easy to extend
* Auto-generated interactive API docs (`/docs`)

---

## 📂 Project Structure

```
.
├── mini_project.py
├── requirements.txt
├── .venv
└── .env
```

---

## 🔧 Requirements

Install dependencies:

```bash
pip install fastapi uvicorn python-decouple langchain-google-genai langchain
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root:

```
GOOGLE_GEMINI_KEY=YOUR_API_KEY_HERE
```

You can obtain your key from:
[https://aistudio.google.com](https://aistudio.google.com)

---

## ▶️ Running the API

Start FastAPI server:

```bash
uvicorn main:app --reload
```

Open interactive docs:

```
http://127.0.0.1:8000/docs
```

---

## 🔥 API Endpoint

### **POST /recommend**

Recommends the best medical department.

### **Request Body**

```json
{
  "gender": "female",
  "age": 62,
  "symptoms": ["pusing", "mual", "sulit berjalan"]
}
```

### **Response Example**

```json
{
  "recommended_department": "Neurology"
}
```

---

## 🧠 How the AI Works

* LangChain sends a structured medical routing prompt to **Gemini 2.0 Flash**
* Gemini evaluates the patient’s symptoms and chooses the closest matching department
* Only the department name is returned

You can replace the prompt logic anytime inside:

```python
get_department_from_llm()
```

---

## 🛠 Technology Stack

| Component    | Tech                    |
| ------------ | ----------------------- |
| Backend      | FastAPI                 |
| LLM          | Google Gemini 2.0 Flash |
| AI Framework | LangChain               |
| Config       | python-decouple         |

---

## 📌 Example Code Snippet (From main.py)

```python
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=GOOGLE_GEMINI_KEY
)
```
