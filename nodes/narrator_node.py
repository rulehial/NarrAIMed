
from llm.clients.client_llm import get_llm_client_openai
from langchain_core.messages import HumanMessage
from datetime import datetime
from langchain_core.runnables import RunnableLambda
from tools.load_text import load_prompt_template

def get_narrative_node():
    narrative_template = load_prompt_template("prompts/narrativa_3.txt")
    def _run(state):
        formatted_prompt = narrative_template.format(
            patient_id=state["patient_id"],
            fuente=state["fuente"],
            fecha_informe=datetime.now().strftime("%d de %B de %Y"),
            # historial=state["contenido"] or state["historial"]
            historial=state["progresion"]
        )
    

        llm = get_llm_client_openai()
        response = llm.invoke([HumanMessage(content=formatted_prompt)])
        # state["narrativa"] = response.content
        state["narrativa"] = response
        return state
    return RunnableLambda(_run)




   