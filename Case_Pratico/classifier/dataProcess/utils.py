import os
from dotenv import load_dotenv
from pathlib import Path

def getEnterpriseName():
    env_path = Path(__file__).resolve().parent.parent.parent.parent / '.envs'
    load_dotenv(dotenv_path=env_path / '.env')
    api_key = os.getenv("NOME_DA_EMPRESA")
    return api_key