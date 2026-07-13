from pypdf import PdfReader

reader = PdfReader("docs/manual.pdf")
texto_extraido = ""

for pagina in reader.pages:
    texto_extraido += pagina.extract_text()

# texto_extraido = texto_extraido.replace("\n", " ")

print(texto_extraido)