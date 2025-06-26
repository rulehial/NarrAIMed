from langchain.prompts import PromptTemplate
# from langgraph.nodes import RunnableNode
# from typing import Dict


from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnableMap
from llm.clients.client_llm import get_llm_client_openai


def medication_node():
    # Prompt para resumir medicación
    prompt = PromptTemplate.from_template( """Extrae las medicacion importantes del siguiente historial:

    {historial}

    Devuelve solo los eventos como lista separada por saltos de línea."""
    )

    llm = get_llm_client_openai()
    chain = prompt | llm
    return RunnableMap({"medicacion": chain})


# def create_medication_summarizer_node():
#     """
#     Nodo LangGraph para resumir la medicación a partir del texto preparado.
#     """

#     def run(state: Dict):
#         medicacion_text = state.get("medicacion_text", "")
#         if not medicacion_text:
#             return "No hay información de medicación disponible."

#         prompt = prompt_template.format(medicacion_text=medicacion_text)

#         # Aquí debes integrar tu LLM, por ejemplo usando Azure OpenAI client o cualquier otro cliente.
#         # Suponiendo que tienes una función llm_invoke que recibe un prompt y devuelve la respuesta:

#         from llm.clients.client_azure import get_llm_client
#         client = get_llm_client()

#         response = client.invoke(prompt)

#         return response.content if hasattr(response, "content") else response

#     return RunnableNode(run)




# def extract_events_node():
#     prompt = PromptTemplate.from_template(
#         """Extrae las constantes vitales y eventos clínicos importantes del siguiente historial:
#         ---
#         {historial}
#         ---
#         Devuelve solo los eventos como lista separada por saltos de línea."""
#     )

#     llm = get_llm_client_openai()
#     chain = prompt | llm
#     return RunnableMap({"eventos": chain})