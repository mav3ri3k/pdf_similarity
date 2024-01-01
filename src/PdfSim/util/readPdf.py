from PyPDF2 import PdfReader

def readPdf(path):
    reader = PdfReader(path)
    full_text = ""
    for page in reader.pages:
        text = page.extract_text()
        full_text += text

    return full_text
