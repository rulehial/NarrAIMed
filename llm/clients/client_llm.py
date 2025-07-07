import logging
from langchain_openai import ChatOpenAI
from config.llm_config import llm_config
logger = logging.getLogger(__name__)

_client_instance = None


def get_llm_client_openai() -> ChatOpenAI:
    """
    Devuelve una instancia singleton del cliente de OpenAI. 
    Inicializa el cliente en la primera llamada.
    """
    global _client_instance
    if _client_instance is None:
        try:
            logger.debug("Initializing OpenAI client...")
            print("Initializing OpenAI client...")
        
            
            _client_instance = ChatOpenAI(        
                api_key=llm_config["api_key"],
                model=llm_config["model_name"], 
                temperature=0.2,
                max_tokens = 5000,
                max_retries=1
            )
            logger.debug("OpenAI client initialized successfully.")
            print("OpenAI client initialized successfully.")
            
        except Exception as e:
            print(f"Failed to initialize OpenAI client: {str(e)}")
            logger.error(f"Failed to initialize OpenAI client: {str(e)}")
            raise RuntimeError(f"Failed to initialize OpenAI client: {str(e)}") from e
            
    return _client_instance