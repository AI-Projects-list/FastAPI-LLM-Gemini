from fastapi import FastAPI
from pydantic import BaseModel
from decouple import config
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import HumanMessage

# -----------------------------------------
# 1. Initialize FastAPI
# -----------------------------------------
app = FastAPI()

# -----------------------------------------
# 2. Load Gemini API Key
# -----------------------------------------
GOOGLE_GEMINI_KEY = config("GOOGLE_GEMINI_KEY")

# -----------------------------------------
# 3. Initialize Gemini LLM
# -----------------------------------------
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=GOOGLE_GEMINI_KEY
)

# -----------------------------------------
# 4. Input Schema (JSON Body)
# -----------------------------------------
class PatientRequest(BaseModel):
    gender: str
    age: int
    symptoms: list[str]

# -----------------------------------------
# 5. Function to Query LLM
# -----------------------------------------
async def get_department_from_llm(gender: str, age: int, symptoms: list[str]) -> str:
    symptom_text = ", ".join(symptoms)

    prompt = f"""
    You are an AI triage assistant in a hospital.
    Recommend the MOST relevant medical department.

    Patient Info:
    - Gender: {gender}
    - Age: {age}
    - Symptoms: {symptom_text}

    Possible departments: Neurology.

    Respond ONLY with the department name.
    """

    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content.strip()

# -----------------------------------------
# 6. API Endpoint
# -----------------------------------------
@app.post("/recommend")
async def recommend_department(patient: PatientRequest):
    department = await get_department_from_llm(
        patient.gender,
        patient.age,
        patient.symptoms
    )

    return {
        "recommended_department": department
    }
