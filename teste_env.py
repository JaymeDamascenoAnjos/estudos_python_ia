import os
import openai
from dotenv import load_dotenv
#
load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 1. Lista de dados para automação (Simulando uma planilha ou banco de dados)
feedbacks = [
    "O app trava toda vez que tento fazer login.",
    "A entrega chegou 2 dias antes do prazo, excelente!",
    "O preço é justo, mas a interface poderia ser mais limpa.",
    "Não consigo cancelar minha assinatura pelo site."
]

print("--- Iniciando Classificação Automática ---\n")

# 2. Loop de Automação
for item in feedbacks:
    # Chamada para a Inteligência Artificial
    resposta = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Classifique o sentimento em uma única palavra: POSITIVO, NEGATIVO ou NEUTRO."},
            {"role": "user", "content": item}
        ]
    )
    
    sentimento = resposta.choices[0].message.content
    print(f"Feedback: {item}")
    print(f"Sentimento: {sentimento}\n")

print("--- Processamento Concluído ---")
