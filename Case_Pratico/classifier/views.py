from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from PyPDF2 import PdfReader
from dataManipulation import removeStopWords, stemmingWords

class ProcessedEmail:
    personName: str
    relevant: bool
    email: str

def ProcessMensage(email: str, personName: str) -> str:
    #TODO make the ia process to classifier the email
    emailProsseced = removeStopWords(email)
    emailProsseced = stemmingWords(emailProsseced)
    return "Classificado"

def renderHomePage(request: HttpRequest):
    return render(request, 'index.html')

def receiveEmail(request: HttpRequest) -> HttpResponse:
    text = ""
    if request.method == "POST":
        if 'pdf_file' in request.FILES:
            pdf_file = request.FILES['pdf_file']
            reader = PdfReader(pdf_file)
            text = "\n".join(page.extract_text() for page in reader.pages if page.extract_text())

        elif 'txt_file' in request.FILES:
            txt_file = request.FILES['txt_file']
            text = txt_file.read().decode('utf-8')

        elif 'email' in request.POST:
            nome = request.POST.get('nome')
            email = request.POST.get('email')
            text = f"Nome: {nome}\nEmail: {email}"
        return render(request, 'index.html', {'text': text})
    return render(request, 'index.html')

