import os
from dotenv import load_dotenv
from pathlib import Path
from google import genai
from google.genai.types import HttpOptions, GenerateContentResponse
import re

def getApiKey():
    env_path = Path(__file__).resolve().parent.parent.parent / '.envs'
    load_dotenv(dotenv_path=env_path / '.env') # Especifique o nome do arquivo .env
    api_key = os.getenv("API_KEY")
    return api_key

APIKEY = getApiKey()
MODEL_NAME = "gemini-2.0-flash-001"
CLIENT = genai.Client(api_key=APIKEY, http_options=HttpOptions(api_version="v1"))

def generateResponse(msg: str) -> GenerateContentResponse:
    response = CLIENT.models.generate_content(
        model=MODEL_NAME,
        contents=msg,
    )
    return response


def checkImportance(msg: str) -> bool:
    #TODO make the corect prompt for the gemini
    prompt = f'''Verifique se a mensagem que passou por um processo de remoção de palavras de parada e stemming é relevanta:\n{msg}\n
                responda apenas sim ou não sem pular linha'''
    response = generateResponse(prompt)
    responseFormated = re.search(r'^\s*(.*?)\s*$', response.text.lower(), re.M)
    if responseFormated.group(1).strip() == 'sim':
        return True
    return False

def ResponseMensage(msg: str, name: str) -> bool:
    #TODO make the corect prompt for the gemini
    prompt = f"gere uma resposta a seguinte pergunta para {name}: {msg}"
    response = generateResponse(prompt)
    return response.text






