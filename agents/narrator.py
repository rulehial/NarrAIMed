from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnableMap
from llm.clients.client_llm import get_llm_client_openai
from langchain_core.messages import HumanMessage
from datetime import datetime
from langchain_core.runnables import Runnable, RunnableLambda
from tools.load_text import load_prompt_template

def generate_narrative_node():
#     prompt = PromptTemplate.from_template(
#         """Redacta un informe clínico narrativo con base en los siguientes contenidos:
#         ---
#         {contenido}
#         ---
#         Sé claro, médico y coherente.
#         """
#     )

#     llm = get_llm_client_openai()
#     chain = prompt | llm
#     return RunnableMap({"narrativa": chain})


    narrative_template = load_prompt_template("prompts/narrativa_4.txt")
    def _run(state):
        formatted_prompt = narrative_template.format(
            patient_id=state["patient_id"],
            fuente=state["fuente"],
            fecha_informe=datetime.now().strftime("%d de %B de %Y"),
            historial=state["contenido"] or state["historial"]
        )
    

        llm = get_llm_client_openai()
        response = llm.invoke([HumanMessage(content=formatted_prompt)])
        state["narrativa"] = response.content
        return state
    return RunnableLambda(_run)




   