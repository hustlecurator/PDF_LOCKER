from PyPDF2 import PdfFileWriter, PdfFileReader
from getpass import getpass

# создаем объекты класса
pdfwriter = PdfFileWriter()
pdf = PdfFileReader('stm32f103c8.pdf')

# получаем все страницы файла
for page in range(pdf.numPages):
    pdfwriter.add_page(pdf.pages[page])

# запрашиваем пароль для шифра
password = getpass(prompt='Input password: ')

# шифруем
pdfwriter.encrypt(password)

with open('stm32f103c8(protected).pdf', 'wb') as file:
    pdfwriter.write(file)
