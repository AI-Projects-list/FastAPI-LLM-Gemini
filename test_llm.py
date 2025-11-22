from decouple import config
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import HumanMessage

GOOGLE_GEMINI_KEY = config("GOOGLE_GEMINI_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=GOOGLE_GEMINI_KEY
)

response = llm.invoke([HumanMessage(content="Hello, what is 2+2? What your name? What LLM type are you?")])
print("Gemini Response:", response.content)
