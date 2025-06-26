from langchain.prompts import PromptTemplate
# from langgraph.nodes import RunnableNode
# from typing import Dict


from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnableMap
from llm.clients.client_llm import get_llm_client_openai


def medication_node():
    # Prompt para resumir medicación
    prompt = PromptTemplate.from_template( """Extrae los exámenes de laboratorio importantes del siguiente historial:

    {historial}

    Devuelve solo los eventos como lista separada por saltos de línea."""
    )

    llm = get_llm_client_openai()
    chain = prompt | llm
    return RunnableMap({"laboratorio": chain})