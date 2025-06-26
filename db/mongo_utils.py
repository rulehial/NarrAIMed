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
                "ID_PACIENTE": 1234,
                "FUENTE": "F_24_04_2020"
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
        {
            "$lookup": {
                "from": "medicacion",
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
                "as": "medicacion"
            }
        },
        {
            "$lookup": {
                "from": "laboratorio",
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
                "as": "laboratorio"
            }
        },
        {
            "$lookup": {
                "from": "cie10_ingreso",
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
                    },
                    {
                        "$project":{
                        "DIA_PPAL_NORMA":1
                        }
                    },
                    {
                        "$lookup": {
                        "from": "cie10_diagnostico",
                        "localField": "DIA_PPAL_NORMA",  
                        "foreignField": "CODIGO",        
                        "as": "diagnostico_ppal"
                        }
                    },
                    {
                        "$unwind": {
                        "path": "$diagnostico_ppal",
                        "preserveNullAndEmptyArrays": True
                        }
                    }
                ],
                "as": "cie10_ingreso"
            }
        }

    ]

    # records = list(collection.find({"ID_PACIENTE": patient_id,"FUENTE" : fuente}))
    records = list(collection.aggregate(pipeline))
    # return pd.DataFrame(records)
    return records