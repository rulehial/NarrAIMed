from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnableMap
from llm.clients.client_llm import get_llm_client_openai

def extract_events_node():
    prompt = PromptTemplate.from_template(
        """Extrae las constantes vitales y eventos clínicos importantes del siguiente historial:
        ---
        {historial}
        ---
        Devuelve solo los eventos como lista separada por saltos de línea."""
    )

    llm = get_llm_client_openai()
    chain = prompt | llm
    return RunnableMap({"eventos": chain})