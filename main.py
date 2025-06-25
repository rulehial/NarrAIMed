from graph.graph_narrative import build_narrative_graph
from db.mongo_utils import get_patient_data  # función que consulta MongoDB
from tools.pepare_data import prepare_historial_for_llm
from pprint import pprint

# 1. Definir identificadores del paciente
patient_id = 1234
fuente = "F_24_04_2020"

# 2. Consultar historial desde MongoDB
data = get_patient_data(patient_id, fuente)

historial = prepare_historial_for_llm(data)




# print("historial--> ", historial)

# pprint(historial)


# 3. Construir grafo
graph = build_narrative_graph()

# 4. Crear input para el grafo
input_data = {
    "historial": historial,
    "patient_id": patient_id,
    "fuente": fuente
}

# 5. Ejecutar el grafo
result = graph.invoke(input_data)

# 6. Mostrar resultado
pprint(result)
