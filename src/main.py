from dotenv import load_dotenv
# from langchain.agents import create_agent
# from langchain_google_genai import GoogleGenerativeAIEmbeddings
# from langchain_community.vectorstores import FAISS
# from utils import read_pdf, split_documents
from knowledge_base import create_vector_store, get_context
from agent import create_mi_tiendita_agent, get_agent_response

load_dotenv()


file = "docs/manual.pdf"

print("\n" + "=" * 60)
print("🌱 MI TIENDITA - ASISTENTE")
print("=" * 60)

question =  input("Haz una pregunta sobre Mi Tiendita: ")

vector_store = create_vector_store(file)

context = get_context(vector_store, question)

agent = create_mi_tiendita_agent(context)

response = get_agent_response(agent, question)

print("\n🤖 Respuesta:")
print(response)
print("\n" + "=" * 60)