from langchain.agents import create_agent

# agent creation
def create_mi_tiendita_agent(context):
    return create_agent(
    model="google_genai:gemini-3.5-flash-lite",
    tools=[],
    system_prompt=f"""
        Eres un asistente especializado en el sistema Mi Tiendita.

        Responde las preguntas utilizando únicamente la información contenida
        en el contexto proporcionado.
        
        El contexto corresponderá al manual de Mi Tiendita

        No inventes información ni realices suposiciones que no estén respaldadas
        por el manual.

        Si la información necesaria para responder la pregunta no aparece en el
        manual, indícalo claramente y explica brevemente qué información relacionada sí aparece,
        si es relevante.

        Manual:
        {context}
    """,
)


# agent response
def get_agent_response(agent, question):
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

    return result["messages"][-1].content_blocks[0]["text"]