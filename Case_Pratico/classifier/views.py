from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from PyPDF2 import PdfReader
from .dataManipulation import removeStopWords, stemmingWords
from .aiProcess import checkImportance, ResponseMensage

class ProcessedEmail:
    def __init__(self, personName: str, relevant: bool, email: str, response: str):
        self.personName = personName
        self.relevant = relevant
        self.email = email
        self.response = response

def ProcessMensage(personName: str, email: str) -> ProcessedEmail:
    emailProsseced = removeStopWords(email)
    emailProsseced = stemmingWords(emailProsseced)
    relevance = checkImportance(emailProsseced)
    if not relevance:
        return ProcessedEmail(personName, relevance, email, "")
    response = ResponseMensage(email, personName)
    return ProcessedEmail(personName, relevance, email, response)
    
def renderHomePage(request: HttpRequest):
    return render(request, 'index.html')

def receiveEmail(request: HttpRequest) -> HttpResponse:
    text = ""
    if request.method == "POST":
        name = request.POST.get('nome')
        if 'pdf_file' in request.FILES:
            pdf_file = request.FILES['pdf_file']
            reader = PdfReader(pdf_file)
            #text = "\n".join(page.extract_text() for page in reader.pages if page.extract_text())

        elif 'txt_file' in request.FILES:
            txt_file = request.FILES['txt_file']
            text = txt_file.read().decode('utf-8')

        elif 'email' in request.POST:
            text = request.POST.get('email')
            #text = f"Nome: {name}\nEmail: {email}"
        responseMensage = ProcessMensage(name, text)
        return render(request, 'simple_response.html', {'text': responseMensage.relevant, 'dirt': responseMensage.response})
    return render(request, 'simple_response.html')

