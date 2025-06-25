from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnableMap
from llm.clients.client_llm import get_llm_client_openai

def analyze_timeline_node():
    prompt = PromptTemplate.from_template(
        """Analiza esta lista de eventos clínicos para detectar progresión o patrones relevantes:
        ---
        {eventos}
        ---
        Devuelve un resumen con posibles cambios clínicos importantes."""
    )

    llm = get_llm_client_openai()
    chain = prompt | llm
    return RunnableMap({"progresion": chain})
