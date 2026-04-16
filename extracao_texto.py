import openai
import json
from dotenv import load_dotenv


# Carregar Chave
load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Texto "sujo" que simula um e-mail ou documento
texto_entrada = "Olá, meu nome é João Silva, moro em São Paulo e acabei de comprar um curso de Python por R$ 450,00."

# O Pulo do Gato: O System Prompt rígido
prompt_sistema = """
Extraia as informações do texto e retorne APENAS um JSON com as chaves: 
'nome', 'cidade', 'produto' e 'valor_numérico'.
Não escreva mais nada além do JSON.
"""
response = client.chat.completions.create(
    model="gpt-3.5-turbo", # ou gpt-4
    messages=[
        {"role": "system", "content": prompt_sistema},
        {"role": "user", "content": texto_entrada}
    ],
    response_format={ "type": "json_object" } # Isso garante que venha um JSON
)

# Transformando a string da IA em um Dicionário Python real
dados_extraidos = json.loads(response.choices[0].message.content)

print(f"Nome extraído: {dados_extraidos['nome']}")
print(f"Valor: {dados_extraidos['valor_numérico']}")
