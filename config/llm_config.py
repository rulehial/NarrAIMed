from dotenv import load_dotenv
import os
import logging
logger = logging.getLogger(__name__)

load_dotenv()


llm_config = {}

print(os.getenv("LLM_TYPE"))
print(os.getenv("MODEL_NAME"))

llm_config.update({
    "api_key": os.getenv("API_KEY"), 
    "model_name": os.getenv("MODEL_NAME")
})
print("Cargando Cliente OpenAI")
logger.debug("Cargando Cliente OpenAI")
# print("NOMBRE MODELO",os.getenv("MODEL_NAME"))



required_vars = ["LLM_TYPE"]
missing_vars = [var for var in required_vars if not os.getenv(var)] # Lista de variables requeridas
# Verificar si faltan variables de entorno
if missing_vars:
    raise ValueError(f"Faltan las siguientes variables de entorno: {', '.join(missing_vars)}")