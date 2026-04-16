import os
import csv
import openai
from dotenv import load_dotenv

load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

ARQUIVO_ENTRADA = "feedbacks_entrada.txt"
ARQUIVO_SAIDA = "analise_sentimentos.csv"

# 1. Ler os dados do TXT
with open(ARQUIVO_ENTRADA, "r", encoding="utf-8") as f:
    frases = [linha.strip() for linha in f.readlines() if linha.strip()]

# 2. Criar o arquivo CSV e processar os dados
with open(ARQUIVO_SAIDA, "w", newline="", encoding="utf-8-sig") as f_csv:
    # Definimos os nomes das colunas (Header)
    campos = ["Texto Original", "Classificacao", "Sugestao_Acao"]
    escritor = csv.DictWriter(f_csv, fieldnames=campos, delimiter=";")
    escritor.writeheader()

    print(f"📊 Gerando planilha: {ARQUIVO_SAIDA}...")

    for frase in frases:
        # Pedindo uma análise mais rica para a IA
        resposta = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Responda no formato: SENTIMENTO | AÇÃO. Exemplo: NEGATIVO | SUPORTE. Use apenas 1 palavra para cada campo."},
                {"role": "user", "content": f"Analise: {frase}"}
            ]
        )

        resultado = resposta.choices[0].message.content.split("|")
        sentimento = resultado[0].strip()
        acao = resultado[1].strip() if len(resultado) > 1 else "N/A"

        # Escrevendo a linha na planilha
        escritor.writerow({
            "Texto Original": frase,
            "Classificacao": sentimento,
            "Sugestao_Acao": acao
        })
        
        print(f"✔ Item processado: {sentimento}")

print("\n🚀 Planilha gerada com sucesso! Abra o arquivo .csv no Excel ou VS Code.")


# Por que isso é importante:
# csv.DictWriter: Facilita a escrita mapeando os dados como um dicionário Python (chave: valor).
# encoding="utf-8-sig": Esse "sig" no final é o segredo para o Excel do Windows abrir o arquivo com os acentos perfeitos.
# delimiter=";": Usamos ponto e vírgula porque é o padrão brasileiro para CSVs que abrem direto no Excel.

# Próximo Passo:
# Rode o código e tente abrir o arquivo analise_sentimentos.csv.