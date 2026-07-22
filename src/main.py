from dotenv import load_dotenv
from pypdf import PdfReader
from langchain.agents import create_agent

load_dotenv()


def read_pdf(file):
    reader = PdfReader(file)
    text = ""

    for page in reader.pages:
        text += page.extract_text()

    return text


manual = read_pdf("docs/manual.pdf")


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