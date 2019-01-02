# PyPDF2 cannot extract text from PDF file when image in it. 
import PyPDF2

print('Please input the PDF path:')
pdfPath = input()

pdfFileObj = open(pdfPath,'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)

pageObj = pdfReader.getPage(1)
print(pageObj.extractText())