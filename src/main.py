from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from utils import read_pdf, split_documents

load_dotenv()


file = "docs/manual.pdf"
manual = read_pdf(file)
chunks = split_documents(manual)

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
)

vector_store = FAISS.from_documents(
    documents=chunks,
    embedding=embeddings
)

print("\n" + "=" * 60)
print("🌱 MI TIENDITA - ASISTENTE")
print("=" * 60)

question =  input("Haz una pregunta sobre Mi Tiendita: ")

results = vector_store.similarity_search(
    question,
    k=3
)

context = "\n\n".join(
    result.page_content
    for result in results
)


agent = create_agent(
    model="google_genai:gemini-3.5-flash-lite",
    tools=[],
    system_prompt=f"""
        Eres un asistente especializado en el sistema Mi Tiendita.

        Responde las preguntas utilizando únicamente la información contenida
        en el contexto proporcionado.

        No inventes información ni realices suposiciones que no estén respaldadas
        por el contexto.

        Contexto:
        {context}
    """,
)


result = agent.invoke(
    {
        "messages": 
        [
            {
                "role": "user", 
                "content": question,
            }
        ]
    }
)

response = result["messages"][-1].content_blocks[0]["text"]

print("\n🤖 Respuesta:")
print(response)
print("\n" + "=" * 60)