import pdfplumber
with pdfplumber.open('wwl.pdf')as pdf:
    for i in pdf.pages:
        print(i.extract_text())
        print('-'*50,end=' ')
        print(f'第{i}页结束')