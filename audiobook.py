import pyttsx3
import PyPDF2

book = open('oop.pdf', 'rb')
pdfREader = PyPDF2.PdfFileReader(book)
pages = pdfREader.numPages
print(pages)

for PG in range(2, pages):
    talkinf = pyttsx3.init()
    page = pdfREader.getPage(2)
    text = page.extractText()
    talkinf.say(text)
    talkinf.runAndWait()

