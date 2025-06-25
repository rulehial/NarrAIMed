from langchain_core.runnables import RunnableLambda

def build_prompt_node():
    def combine(state):
        return {
            "contenido": f"""Paciente ID: {state['patient_id']}, Fuente: {state['fuente']}
            Eventos: {state['eventos']}
            Progresión: {state.get('progresion', '')}
            """
        }

    return RunnableLambda(combine)