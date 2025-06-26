from langchain_core.runnables import RunnableLambda

def build_prompt_node():
    def combine(state):
        return {
            "contenido": f"""Paciente ID: {state['patient_id']}, Fuente: {state['fuente']}
            Eventos: {state['eventos']}
            Medicación: {state['medicacion']}
            Examenes de Laboratorio : {state['laboratorio']}
            Progresión: {state.get('progresion', '')}
            Diagniostico Segun CIE- 10: {state.get('diagnostico_cie10', '')}
            """
        }

    return RunnableLambda(combine)