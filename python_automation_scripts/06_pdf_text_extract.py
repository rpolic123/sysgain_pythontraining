import PyPDF2

with open('sample.pdf', 'rb') as f:
    reader = PyPDF2.PdfReader(f)
    for page in reader.pages:
        print(page.extract_text())