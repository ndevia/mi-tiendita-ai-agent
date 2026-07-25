from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from utils import read_pdf, split_documents


# vector store
def create_vector_store(file):
    manual = read_pdf(file)
    chunks = split_documents(manual)

    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001"
    )

    return FAISS.from_documents(
        documents=chunks,
        embedding=embeddings
    )


# context
def get_context(vector_store, question, k=3):
    results = vector_store.similarity_search(question, k=k)

    return "\n\n".join(
        result.page_content
        for result in results
    )