from graph.graph_narrative import build_narrative_graph
from db.mongo_utils import get_patient_data, get_fuentes_data  
from tools.pepare_data import prepare_historial_for_llm, format_eventos_for_llm, format_medicacion_for_llm, format_laboratorio_for_llm, prepare_diagnostico_ppal
import streamlit as st
from datetime import datetime


fuentes_disponibles = [doc['_id'] for doc in get_fuentes_data()]

st.title("NarrAIMed: Generador de Informes Clínicos Narrativos")

# Inputs del usuario
patient_id = st.text_input("Ingrese ID del paciente", "")
fuente = st.selectbox("Seleccione la fuente del informe", fuentes_disponibles)

spinner_placeholder = st.empty()

st.spinner("🔄 Consultando datos del paciente...")

if st.button("Generar narrativa"):
    if patient_id and fuente:

        with st.spinner("👨‍⚕️ Pusimos a trabajar a nuestro médico...."):
            spinner_placeholder.info("🔄 Consultando datos del paciente...")
            
            # Obtenem,os los datos e historial del paciente desde MongoDB
            
            paciente_data = get_patient_data(patient_id, fuente)
            
            #Chequeamos que el paciente existe
            if paciente_data:
                paciente = paciente_data[0]           


                historial = prepare_historial_for_llm(paciente_data)
                eventos_data = paciente.get("eventos", [])
                medicacion_data = paciente.get("medicacion", [])
                laboratorio_data = paciente.get("laboratorio", [])
                cie10_ingreso_data = paciente.get("cie10_ingreso", [])


                # Prepararlos para llm
                eventos = format_eventos_for_llm(eventos_data)
                medicacion = format_medicacion_for_llm(medicacion_data)
                laboratorio = format_laboratorio_for_llm(laboratorio_data)
                diagnostico_cie10 = prepare_diagnostico_ppal(cie10_ingreso_data)


                spinner_placeholder.info("🧠 Generando narrativa clínica...")

                #  Construir grafo
                graph = build_narrative_graph()

                # Crear input para entrada del grafo
                input_data = {
                    "historial": historial,
                    "eventos": eventos,
                    "medicacion": medicacion,
                    "laboratorio": laboratorio,
                    "diagnostico_cie10": diagnostico_cie10,
                    "patient_id": patient_id,
                    "fuente": fuente,
                }

                # Ejecutar el grafo
                result = graph.invoke(input_data) 
                narrativa = result["narrativa"]


                spinner_placeholder.success("✅ Narrativa generada exitosamente.")

                # Imprimimos narrativa
                st.subheader("📄 Informe Narrativo")
                st.markdown(narrativa)
                print(narrativa,  file=open(f'narrativas\{patient_id}__{fuente}__{datetime.now().strftime("%Y_%m_%d__%H_%M_%S")}.txt', 'w',encoding="utf-8"))
            else:
                st.warning("🕵️‍♀️ No se encontró el paciente.")
    else:
        st.warning("✏️ Por favor ingrese ambos campos.")