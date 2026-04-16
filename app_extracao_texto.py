import os
import streamlit as st
import json
import pandas as pd # Essencial para manipular dados e gerar o CSV
import openai
from dotenv import load_dotenv


# 1. Configuração da API (Coloque sua chave aqui ou no Secrets do Streamlit)
load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("🚀 Extrator de Dados Inteligente")
st.subheader("Transforme textos bagunçados em planilhas limpas")

# 2. Área de entrada de texto
texto_bruto = st.text_area("Cole aqui o texto do e-mail, contrato ou anotação:", height=200)

if st.button("Extrair e Gerar Planilha"):
    if texto_bruto:
        with st.spinner('A IA está lendo o texto...'):
            # 3. O Prompt "Mágico" para garantir o JSON
            prompt_sistema = """
            Você é um especialista em extração de dados. 
            Extraia as informações do texto e retorne APENAS um JSON com as chaves: 
            'nome_completo', 'email', 'telefone', 'empresa' e 'valor_estimado'.
            Se não encontrar algum dado, preencha com 'Não informado'.
            Não escreva nenhuma saudação ou explicação, apenas o JSON puro.
            """

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                response_format={ "type": "json_object" }, # Força o formato JSON
                messages=[
                    {"role": "system", "content": prompt_sistema},
                    {"role": "user", "content": texto_bruto}
                ]
            )

            # 4. Transformando a resposta da IA em um Dicionário Python
            dados_json = json.loads(response.choices[0].message.content)
            
            # 5. Transformando em DataFrame (Tabela) para o Streamlit e CSV
            df = pd.DataFrame([dados_json])

            st.success("Dados extraídos com sucesso!")
            st.table(df) # Exibe a tabela bonitinha no App

            # 6. Gerando o botão de download do CSV
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Baixar dados em CSV (Excel)",
                data=csv,
                file_name='dados_extraidos.csv',
                mime='text/csv',
            )
    else:
        st.warning("Por favor, cole algum texto primeiro.")
