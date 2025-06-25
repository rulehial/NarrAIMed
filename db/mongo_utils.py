# Conexión a Mongo y funciones de lectura

from pymongo import MongoClient
import os
import pandas as pd
from dotenv import load_dotenv
load_dotenv()


client = MongoClient(os.getenv("MONGO_URI"))
db = client[os.getenv("MONGO_DB_NAME")]


def get_patient_data(patient_id: int, fuente: str):
    # print(patient_id, fuente)
    # ingreso = db["ingresos"].find_one({"ID_PACIENTE": patient_id, "FUENTE": fuente})

    # print(ingreso)
    # constantes = list(db["constantes_vitales"].find({"ID_PACIENTE": patient_id, "FUENTE": fuente}))
    # return ingreso, constantes

    collection = db["ingresos"]

    pipeline =[
        {
            "$match": {
                "ID_PACIENTE": patient_id,
                "FUENTE": fuente
            }
        },
        {
            "$lookup": {
                "from": "constantes_vitales",
                "let": {
                    "id_paciente": "$ID_PACIENTE",
                    "fuente": "$FUENTE"
                },
                "pipeline": [
                    {
                        "$match": {
                            "$expr": {
                                "$and": [
                                    { "$eq": ["$ID_PACIENTE", "$$id_paciente"] },
                                    { "$eq": ["$FUENTE", "$$fuente"] }
                                ]
                            }
                        }
                    }
                ],
                "as": "eventos"
            }
        },
    ]

    # records = list(collection.find({"ID_PACIENTE": patient_id,"FUENTE" : fuente}))
    records = list(collection.aggregate(pipeline))
    # return pd.DataFrame(records)
    return records