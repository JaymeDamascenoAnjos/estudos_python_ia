from PyPDF2 import PdfReader

# Substitua pelo nome do seu arquivo
reader = PdfReader("Bradesco_04032019_145646.pdf")
texto_completo = ""

for page in reader.pages:
    texto_completo += page.extract_text()

print(texto_completo[:500]) # Mostra apenas os primeiros 500 caracteres
