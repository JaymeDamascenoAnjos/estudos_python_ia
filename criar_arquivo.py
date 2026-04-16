import os
import openai
from dotenv import load_dotenv

load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

feedbacks = [
    "O app trava toda vez que tento fazer login.",
    "A entrega chegou 2 dias antes do prazo, excelente!",
    "O preço é justo, mas a interface poderia ser mais limpa.",
    "Não consigo cancelar minha assinatura pelo site."
]

# Criando (ou sobrescrevendo) o arquivo de texto
#with open("relatorio_sentimentos.txt", "w", encoding="utf-8") as arquivo:
with open("relatorio_sentimentos.txt", "a", encoding="utf-8") as arquivo:    
    arquivo.write("RELATÓRIO DE ANÁLISE DE FEEDBACK\n")
    arquivo.write("="*30 + "\n\n")

    print("Processando e salvando no arquivo...")

    for item in feedbacks:
        resposta = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Classifique o sentimento: POSITIVO, NEGATIVO ou NEUTRO."},
                {"role": "user", "content": item}
            ]
        )
        
        sentimento = resposta.choices[0].message.content
        
        # Escrevendo no arquivo
        linha = f"Feedback: {item}\nSentimento: {sentimento}\n" + "-"*10 + "\n"
        arquivo.write(linha)
        
        # Mostra no terminal para você acompanhar o progresso
        print(f"✔ Processado: {item[:30]}...")

print("\n--- Concluído! Verifique o arquivo 'relatorio_sentimentos.txt' no seu VS Code. ---")


# Sensacional! Você acaba de completar o ciclo completo de uma automação básica:
# Entrada (Lista de feedbacks).
# Processamento Inteligente (LLM da OpenAI).
# Persistência de Dados (Salvando em arquivo .txt).