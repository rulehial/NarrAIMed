from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnableMap
from llm.clients.client_llm import get_llm_client_openai

def generate_narrative_node():
    prompt = PromptTemplate.from_template(
        """Redacta un informe clínico narrativo con base en los siguientes contenidos:
        ---
        {contenido}
        ---
        Sé claro, médico y coherente.
        """
    )

    llm = get_llm_client_openai()
    chain = prompt | llm
    return RunnableMap({"narrativa": chain})
