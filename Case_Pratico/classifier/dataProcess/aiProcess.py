import os
from dotenv import load_dotenv
from pathlib import Path
from google import genai
from google.genai.types import HttpOptions, GenerateContentResponse
import re

def getApiKey():
    env_path = Path(__file__).resolve().parent.parent.parent.parent / '.envs'
    load_dotenv(dotenv_path=env_path / '.env')
    api_key = os.getenv("API_KEY")
    return api_key

def getEnterpriseName():
    env_path = Path(__file__).resolve().parent.parent.parent.parent / '.envs'
    load_dotenv(dotenv_path=env_path / '.env')
    api_key = os.getenv("NOME_DA_EMPRESA")
    return api_key

ENTERPRICE_NAME = getEnterpriseName()
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
    prompt = f'''Verifique a relevância da seguinte mensagem para a {ENTERPRICE_NAME}, uma empresa do setor financeiro que atua em [inserir aqui o foco da empresa, ex: gestão de investimentos e consultoria financeira].
                Considere que mensagens relevantes exigem uma ação imediata ou estão diretamente ligadas a:
                * Novas oportunidades de investimento ou consultoria
                * Propostas de produtos/serviços financeiros
                * Dúvidas ou solicitações de clientes sobre contas, investimentos ou produtos existentes
                * Parcerias estratégicas no mercado financeiro
                * Assuntos regulatórios ou de conformidade

                Ignore mensagens de felicitações, agradecimentos, propagandas irrelevantes, ou qualquer conteúdo não diretamente relacionado às operações e serviços financeiros da {ENTERPRICE_NAME}.
                Mensagem:
                {msg}

                Responda apenas "Sim" ou "Não".
              '''
    response = generateResponse(prompt)
    responseFormated = re.search(r'^\s*(.*?)\s*$', response.text.lower(), re.M)
    if responseFormated.group(1).strip() == 'sim':
        return True
    return False

def responseMensage(msg: str, name: str) -> bool:
    prompt = f'''Como a {ENTERPRICE_NAME}, uma empresa financeira especializada em [inserir aqui o foco principal da empresa, ex: gestão de investimentos, planejamento patrimonial e soluções de crédito], **redija o conteúdo HTML de um e-mail profissional e completo para {name}**. A mensagem de {name} é a seguinte:
                Mensagem:
                {msg}

                O e-mail deve ser formatado em HTML como uma string, usando tags `<p>` para parágrafos, `<strong>` para destaques importantes e, se relevante, `<ul><li>` para listas.

                O conteúdo HTML deve incluir:
                1. Uma **saudação inicial** personalizada (ex: `<p>Prezado(a) {name},</p>`).
                2. Um **corpo do e-mail** que:
                    * Responda à mensagem de {name} de forma clara, útil e empática.
                    * Reflita nosso compromisso em fornecer **soluções financeiras inteligentes, personalizadas e que ajudem a alcançar objetivos**.
                    * Foque em como a {ENTERPRICE_NAME} pode **agregar valor, auxiliar na tomada de decisões financeiras, ou resolver desafios específicos**.
                    * Sugira **próximos passos claros**, como agendamento de uma conversa, solicitação de mais informações ou apresentação de uma proposta.
                3. Um **encerramento cordial** (ex: `<p>Atenciosamente,<br>Equipe {ENTERPRICE_NAME}</p>`).

                Gere apenas o conteúdo HTML que seria colocado dentro da tag `<body>`. Não inclua `<html>`, `<head>`, `<body>` ou `<!DOCTYPE>`. Certifique-se de que todas as tags HTML estejam corretamente fechadas.
'''
    response = generateResponse(prompt)
    print(response.text)
    responseFormated = re.sub(r'^```html\s*', '', response.text, flags=re.MULTILINE)
    responseFormated = re.sub(r'\s*```$', '', responseFormated, flags=re.MULTILINE)
    print(responseFormated)
    return responseFormated

def generateSubject(msg: str) -> str:
    prompt = "Gere um assunto breve para o seguinte email"
    response = generateResponse(prompt)
    responseFormated = re.search(r'^\s*(.*?)\s*$', response.text.lower(), re.M)
    return responseFormated.group(1).strip()



