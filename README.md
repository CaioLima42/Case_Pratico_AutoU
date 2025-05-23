# 📁 Case_Pratico_AutoU

Esta é a minha solução para o *case prático* proposto pela empresa **AutoU**.

## ⚙️ Requisitos

- Python 3.11+
- pip
- Virtualenv (opcional, mas recomendado)

## 📦 Instalação

### 1. Clone o repositório

```
git clone https://github.com/seu-usuario/case_pratico_autou.git
cd case_pratico_autou
```

# Crie e Ative seu ambiente virtual(opcional):

```
python -m venv venv
venv\Scripts\activate
```

# Faça as "migrações" do banco de dados:

```
python manage.py makemigrations
python manage.py migrate
```

# Crie as Variáveis de Ambiente Necessárias:
Na raiz do seu projeto (case_pratico_autou/), crie uma pasta chamada .envs. Dentro dessa pasta, crie um arquivo chamado .env (sem nenhuma extensão).

O conteúdo do arquivo .env deve ser o seguinte. Lembre-se de substituir o texto entre aspas pelas suas informações reais:

```
API_KEY="SUA_CHAVE_DE_API_DO_GEMINI"
EMAIL_ADM_PASSWORD="SUA_SENHA_DE_ACESSO_A_UM_GMAIL"
EMAIL_ADM_ADRESS="SEU_ENDERECO_DE_EMAIL_ADMINISTRADOR"
NOME_DA_EMPRESA="NOME_DA_EMPRESA_DE_FINANCAS"

```

# Inicialize o servidor:

```
python manage.py runserver
```

### 🛠️ Detalhes tecnicos:

# Uso do DJANGO:
Foi escolhido por sua capacidade de integrar de forma simples o backend com o frontend, além de fornecer um robusto suporte a ORM (Object-Relational Mapping). A familiaridade com o framework também contribuiu para esta escolha.

### Uso do Gemini como Ai de processamento:
Selecionado por ser uma IA eficiente e por oferecer prompts ilimitados de forma gratuita, ideal para a classificação de e-mails e sugestão de respostas.

### Uso do smtplib para fazer o envido de emails
Essa biblioteca foi selecionada pelo fato de não precisar ter nenhum aplicativo de email baixado localmente, em contra partida, ela não consegue fazer a comunicação a partir de emails gerenciados pelo outlook

### Uso do nltk para fazer o processamento das mensagens:
Esta é uma biblioteca eficiente para o pré-processamento de mensagens. Nesta aplicação, ela foi utilizada para remover *stop words* e aplicar *stemming*