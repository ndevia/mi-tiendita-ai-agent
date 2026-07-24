from dotenv import load_dotenv
from langchain.agents import create_agent
from utils import read_pdf, split_documents

load_dotenv()


file = "docs/manual.pdf"
manual = read_pdf(file)
chunks = split_documents(manual)

print(f"Cantidad de páginas: {len(manual)}")
print(f"Cantidad de fragmentos: {len(chunks)}")

print("\nPrimer fragmento:")
print(chunks[0].page_content)

print("\nMetadata:")
print(chunks[0].metadata)


agent = create_agent(
    model="google_genai:gemini-3.5-flash-lite",
    tools=[],
    system_prompt=f"""
        Eres un asistente especializado en el sistema Mi Tiendita.

        Responde las preguntas utilizando únicamente la información contenida
        en el siguiente manual.

        No inventes información ni realices suposiciones que no estén respaldadas
        por el manual. Si una información no aparece en el manual, indícalo
        claramente.

        Manual:
        {manual}
    """,
)

question =  input("Haz una pregunta sobre Mi Tiendita: ")

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

print(result["messages"][-1].content_blocks)