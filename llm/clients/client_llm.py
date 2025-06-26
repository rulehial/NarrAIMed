import logging
from langchain_openai import AzureChatOpenAI

from langchain_openai import ChatOpenAI

from config.llm_config import llm_config
logger = logging.getLogger(__name__)

_client_instance = None

def get_llm_client_azure() -> AzureChatOpenAI:
    """
    Returns a singleton instance of the AzureOpenAI client.
    Initializes the client on the first call.
    """
    global _client_instance
    if _client_instance is None:
        try:
            logger.debug("Initializing AzureOpenAI client...")
            print("Initializing AzureOpenAI client...")
            _client_instance = AzureChatOpenAI(
                # api_version=azure_config["api_version"],
                # max_retries=1,
                # model=azure_config["model_name"],
                # temperature=0.8
                api_key=llm_config["api_key"],
                api_version=llm_config["api_version"],
                azure_endpoint=llm_config["azure_endpoint"],
                # model_name=azure_config["model_name"], 
                azure_deployment=llm_config["azure_deployment"],
                temperature=0.2,
                max_tokens = 5000,
                max_retries=1
            )
            logger.debug("AzureOpenAI client initialized successfully.")
            print("AzureOpenAI client initialized successfully.")
        except Exception as e:
            print(f"Failed to initialize AzureOpenAI client: {str(e)}")
            logger.error(f"Failed to initialize AzureOpenAI client: {str(e)}")
            # Re-raise the exception to make it clear initialization failed
            raise RuntimeError(f"Failed to initialize AzureOpenAI client: {str(e)}") from e
            
    return _client_instance


def get_llm_client_openai() -> ChatOpenAI:
    """
    Returns a singleton instance of the AzureOpenAI client.
    Initializes the client on the first call.
    """
    global _client_instance
    if _client_instance is None:
        try:
            logger.debug("Initializing OpenAI client...")
            print("Initializing OpenAI client...")
        
            
            _client_instance = ChatOpenAI(
                # api_version=azure_config["api_version"],
                # max_retries=1,
                # model=azure_config["model_name"],
                # temperature=0.8
                api_key=llm_config["api_key"],
                # api_version=llm_config["api_version"],
                # azure_endpoint=llm_config["azure_endpoint"],
                model_name=llm_config["model_name"], 
                # azure_deployment=llm_config["azure_deployment"],
                temperature=0.2,
                max_tokens = 5000,
                max_retries=1
            )
            logger.debug("OpenAI client initialized successfully.")
            print("OpenAI client initialized successfully.")
            
        except Exception as e:
            print(f"Failed to initialize OpenAI client: {str(e)}")
            logger.error(f"Failed to initialize OpenAI client: {str(e)}")
            # Re-raise the exception to make it clear initialization failed
            raise RuntimeError(f"Failed to initialize OpenAI client: {str(e)}") from e
            
    return _client_instance