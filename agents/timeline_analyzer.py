from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnableMap
from llm.clients.client_llm import get_llm_client_openai

def analyze_timeline_node():
    # prompt = PromptTemplate.from_template(
    #     """Analiza esta lista de eventos clínicos para detectar progresión o patrones relevantes:
    #     ---
    #     {eventos}
    #     ---
    #     Devuelve un resumen con posibles cambios clínicos importantes."""
    # )


    prompt = PromptTemplate.from_template( """
                                                Eres un asistente clínico que analiza la evolución temporal del paciente durante su ingreso hospitalario.

                                                Dispones de la siguiente información:

                                                1. Eventos clínicos cronológicos (como frecuencia cardíaca, presión arterial, temperatura, etc.)
                                                2. Registros de medicación administrada, incluyendo fechas de inicio y fin, nombre del fármaco y tipo.

                                                Información proporcionada:
                                          
                                                --- Datos Generales del Paciente ---
                                                {historial}

                                                --- Eventos Clínicos ---
                                                {eventos}

                                                --- Medicación Administrada ---
                                                {medicacion}
                                          
                                                --- Exámenes de Laboratorio ---
                                                {laboratorio}

                                                Tu tarea es:

                                                - Detectar correlaciones temporales entre eventos clínicos, administración de fármacos y exámenes de laboratorio.
                                                - Identificar tendencias importantes en el estado del paciente (empeoramiento, mejoría, estabilidad).
                                                - Señalar posibles efectos secundarios o respuestas a medicamentos.
                                                - Identificar hitos clínicos relevantes como inicio de fiebre, hipotensión, taquicardia, recuperación, etc.

                                                Devuelve un análisis claro y estructurado sobre la progresión clínica del paciente a lo largo del tiempo, indicando cualquier hallazgo significativo que pueda ser útil para los clínicos.
                                                """
    )



    llm = get_llm_client_openai()
    chain = prompt | llm
    return RunnableMap({"progresion": chain})



