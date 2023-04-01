import PyPDF2

pdf_file = open('Codiceappalti-Dlgs362023.pdf', 'rb')

pdf_reader = PyPDF2.PdfReader(pdf_file)

num_pages = len(pdf_reader.pages)
page_text = []

for page_num in range(0,205):
    page = pdf_reader.pages[page_num]
    page_text.append(page.extract_text())


page_text = "".join(page_text)

with open('appalti.txt', 'w') as f:
    f.write(page_text)

pdf_file.close()