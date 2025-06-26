from dotenv import load_dotenv
import os
import logging

logger = logging.getLogger(__name__)
# Cargar las variables de entorno desde el archivo .env
load_dotenv()                                                   # Carga las variables de entorno desde el archivo .env


llm_config = {}

print(os.getenv("LLM_TYPE"))
print(os.getenv("MODEL_NAME"))
if os.getenv("LLM_TYPE") == 'OPENAI':
    llm_config.update({
        "api_key": os.getenv("API_KEY"), 
        "model_name": os.getenv("MODEL_NAME")
    })
    print("Cargando Cliente OpenAI")
    logger.debug("Cargando Cliente OpenAI")
    # print("NOMBRE MODELO",os.getenv("MODEL_NAME"))
else:
    llm_config.update({
        "api_key": os.getenv("AZURE_OPENAI_API_KEY"),               # Clave de API de Azure OpenAI
        "api_version": os.getenv("AZURE_OPENAI_API_VERSION"),       # Versión de la API de Azure OpenAI
        "azure_endpoint": os.getenv("AZURE_OPENAI_ENDPOINT"),       # Punto de enlace de Azure OpenAI
        "model_name": os.getenv("AZURE_OPENAI_MODEL_NAME"),          # Nombre del modelo de Azure OpenAI
        "azure_deployment": os.getenv("AZURE_OPENAI_GPT4_DEPLOYMENT_NAME"),    # Nombre del depósito de Azure OpenAI
    })
        
    print("Cargando Cliente AzureOpenAI")
    logger.debug("Cargando Cliente AzureOpenAI")

# # Configuración de Azure OpenAI
# azure_config = {
#     "api_key": os.getenv("AZURE_OPENAI_API_KEY"),               # Clave de API de Azure OpenAI
#     "api_version": os.getenv("AZURE_OPENAI_API_VERSION"),       # Versión de la API de Azure OpenAI
#     "azure_endpoint": os.getenv("AZURE_OPENAI_ENDPOINT"),       # Punto de enlace de Azure OpenAI
#     "model_name": os.getenv("AZURE_OPENAI_MODEL_NAME"),          # Nombre del modelo de Azure OpenAI
#     "azure_deployment": os.getenv("AZURE_OPENAI_GPT4_DEPLOYMENT_NAME"),    # Nombre del depósito de Azure OpenAI
# }

# Validar que las variables de entorno estén definidas
# required_vars = ["AZURE_OPENAI_API_KEY", "AZURE_OPENAI_API_VERSION", "AZURE_OPENAI_ENDPOINT", "AZURE_OPENAI_MODEL_NAME"]
required_vars = ["LLM_TYPE"]
missing_vars = [var for var in required_vars if not os.getenv(var)] # Lista de variables requeridas
# Verificar si faltan variables de entorno
if missing_vars:
    raise ValueError(f"Faltan las siguientes variables de entorno: {', '.join(missing_vars)}")