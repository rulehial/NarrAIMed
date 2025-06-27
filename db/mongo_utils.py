# Conexión a Mongo y funciones de lectura

from pymongo import MongoClient
import os
from dotenv import load_dotenv
load_dotenv()


client = MongoClient(os.getenv("MONGO_URI"))
db = client[os.getenv("MONGO_DB_NAME")]


def get_fuentes_data():

    """
    Devuelve las fuentes disponibles

    """
    collection = db["ingresos"]
    pipeline = [
        {
            "$group": {
            "_id": "$FUENTE"
            }
        }
    ]

    records = list(collection.aggregate(pipeline))
    return records


def get_patient_data(patient_id: int, fuente: str):
    """
    Devuelve los datos del paciente con el id dado y la fuente dada

    """
    #Obligoa  que sea entero
    patient_id = int(patient_id)

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

    records = list(collection.aggregate(pipeline))
    return records