import openai
import streamlit as st
import os
from dotenv import load_dotenv

# Configuração da Página
st.set_page_config(page_title="Analista de IA", page_icon="🤖")
st.title("🤖 Analisador de Feedbacks Inteligente")

# Carregar Chave
load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Interface do Usuário
st.subheader("Cole seus feedbacks abaixo (um por linha):")
texto_entrada = st.text_area("Ex: O produto é ótimo!", height=150)

if st.button("Analisar Sentimentos"):
    if texto_entrada.strip():
        # Transforma o texto em lista
        linhas = [l.strip() for l in texto_entrada.split("\n") if l.strip()]
        
        st.write(f"⏳ Processando {len(linhas)} itens...")
        
        # Onde vamos guardar os resultados - LISTAS []
        resultados = []

        for item in linhas:
            # Chamada da IA
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    #{"role": "system", "content": "Classifique em POSITIVO, NEGATIVO ou NEUTRO. Responda apenas a palavra."},
                    {"role": "system", "content": "Você é um crítico de cinema sarcástico. Classifique o sentimento, mas dê uma resposta curta e irônica sobre o texto do usuário."},
                    {"role": "user", "content": item}
                ]
            ) 
            sentimento = response.choices[0].message.content
            resultados.append({"Texto": item, "Sentimento": sentimento}) # DICIONÁRIO {}

        # Exibindo os resultados em uma tabela bonita
        st.success("Análise concluída!")
        st.table(resultados)
        
        # Botão para baixar (Automação de exportação)
        csv_data = "Texto;Sentimento\n" + "\n".join([f"{r['Texto']};{r['Sentimento']}" for r in resultados])
        st.download_button("Baixar Resultados (CSV)", csv_data, "analise.csv", "text/csv")
    else:
        st.warning("Por favor, insira algum texto.")


# Como rodar isso:
# No terminal do VS Code, você não usa python app_analise.py. Você usa:
# streamlit run app_analise.py

# O que você conquistou aqui:
# Frontend: Criou uma interface com botões, área de texto e tabelas sem saber HTML/CSS.
# Interatividade: O usuário agora controla o que a IA processa.
# Entrega de Valor: Você tem um botão de "Download" que entrega o arquivo CSV que aprendemos antes.


