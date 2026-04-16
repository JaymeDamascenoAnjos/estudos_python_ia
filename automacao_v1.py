import os
import openai
from dotenv import load_dotenv

load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Nome dos arquivos
ARQUIVO_ENTRADA = "feedbacks_entrada.txt"
ARQUIVO_SAIDA = "resultados_analise.txt"

print(f"🚀 Iniciando automação de leitura de: {ARQUIVO_ENTRADA}...")

# 1. Lendo o arquivo de entrada
with open(ARQUIVO_ENTRADA, "r", encoding="utf-8") as f_entrada:
    linhas = f_entrada.readlines()

# 2. Abrindo o arquivo de saída para escrever os resultados
with open(ARQUIVO_SAIDA, "w", encoding="utf-8") as f_saida:
    f_saida.write("RELATÓRIO AUTOMATIZADO DE SENTIMENTOS\n")
    f_saida.write("-" * 40 + "\n")

    for i, linha in enumerate(linhas):
        texto = linha.strip() # Remove espaços vazios e quebras de linha
        
        if not texto: continue # Pula linhas vazias

        print(f"Analisando item {i+1}...")

        # Chamada da IA
        resposta = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Responda apenas com: POSITIVO, NEGATIVO ou NEUTRO."},
                {"role": "user", "content": texto}
            ]
        )

        sentimento = resposta.choices[0].message.content.strip()

        # Gravando no arquivo final
        f_saida.write(f"Texto: {texto}\nResultado: {sentimento}\n\n")

print(f"\n✅ Concluído! Resultados salvos em: {ARQUIVO_SAIDA}")



# O que você aprendeu agora:
# readlines(): Como o Python lê um arquivo inteiro e o transforma em uma lista de strings.
# strip(): Limpeza de dados (essencial em automação para evitar erros de formatação).
# Tratamento de Arquivos: Como ler de um lugar e escrever em outro simultaneamente.
# O desafio final da Semana 1: Consegue rodar esse script e ver o resultados_analise.txt aparecer preenchido?