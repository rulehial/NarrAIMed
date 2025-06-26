from graph.graph_narrative import build_narrative_graph
from db.mongo_utils import get_patient_data  # función que consulta MongoDB
from tools.pepare_data import prepare_historial_for_llm, format_eventos_for_llm, format_medicacion_for_llm, format_laboratorio_for_llm, prepare_diagnostico_ppal
from pprint import pprint
from fpdf import FPDF

from datetime import datetime

# 1. Definir identificadores del paciente
patient_id = 1234
fuente = "F_24_04_2020"

# 2. Consultar historial desde MongoDB
data = get_patient_data(patient_id, fuente)

paciente = data[0]

historial = prepare_historial_for_llm(data)
eventos_data = paciente.get("eventos", [])
medicacion_data = paciente.get("medicacion", [])
laboratorio_data = paciente.get("laboratorio", [])
cie10_ingreso_data = paciente.get("cie10_ingreso", [])
# cie10_ingreso = cie10_ingreso_data[0]
# diagnostico_ppal = cie10_ingreso.get("diagnostico_ppal", {})

# print("diagnostico_ppal ----->",diagnostico_ppal)

# print("paciente --->",paciente)

eventos = format_eventos_for_llm(eventos_data)
medicacion = format_medicacion_for_llm(medicacion_data)
laboratorio = format_laboratorio_for_llm(laboratorio_data)
diagnostico_cie10 = prepare_diagnostico_ppal(cie10_ingreso_data)
# print("historial--> ", historial)
# print("Eventos -->",eventos)

# print("medicacion --->", medicacion)
# print("laboratorio --->", laboratorio)

# print("ddpal ----->",diagnostico_cie10)



# print("historial--> ", historial)

# pprint(historial)

# fecha = datetime.now().strftime("%d de %B de %Y")
# 3. Construir grafo
graph = build_narrative_graph()

# 4. Crear input para el grafo
input_data = {
    "historial": historial,
    "eventos": eventos,
    "medicacion": medicacion,
    "laboratorio": laboratorio,
    "diagnostico_cie10": diagnostico_cie10,
    "patient_id": patient_id,
    "fuente": fuente,
}

# 5. Ejecutar el grafo
result = graph.invoke(input_data)

# 6. Mostrar resultado
print("result --->",result)

# 6. Mostrar resultado
# pprint(result["narrativa"].content)
print("narrativa ---->",result["narrativa"])

# print("Tokens ---->",result["narrativa"].response_metadata)


# Ejemplo de uso:
narrativa = result["narrativa"]
# guardar_narrativa_pdf("informe_paciente_1234.pdf", narrativa)


# your_data = {"Purchase Amount": 'TotalAmount'}
print(narrativa,  file=open(f'narrativas\{patient_id}_{fuente}_{datetime.now().strftime("%Y_%m_%d")}.txt', 'w',encoding="utf-8"))