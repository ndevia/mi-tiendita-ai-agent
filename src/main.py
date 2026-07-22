from pypdf import PdfReader

file_path = "docs/manual.pdf"


def read_pdf(file):
    reader = PdfReader(file)
    text = ""

    for page in reader.pages:
        text += page.extract_text()

    return text

text = read_pdf(file_path)
print(text)