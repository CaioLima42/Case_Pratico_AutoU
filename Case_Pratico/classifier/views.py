from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from PyPDF2 import PdfReader
from .dataProcess import removeStopWords, stemmingWords, checkImportance, responseMensage, generateSubject, getEnterpriseName
from .models import CheckedEmail
from .emailSender.send import sendEmail as se
from django.shortcuts import get_object_or_404, redirect

EnterpriceName = getEnterpriseName()
    
class ProcessedEmail:
    def __init__(self, clientEmail: str, relevant: bool, email: str, response: str):
        self.clientEmail = clientEmail
        self.relevant = relevant
        self.email = email
        self.response = response

def ProcessMensage(clientEmail: str, emailContext: str) -> ProcessedEmail:
    emailProsseced = removeStopWords(emailContext)
    emailProsseced = stemmingWords(emailProsseced)
    relevance = checkImportance(emailProsseced)
    if not relevance:
        return ProcessedEmail(clientEmail, relevance, emailContext, "")
    response = responseMensage(emailContext, clientEmail)
    return ProcessedEmail(clientEmail, relevance, emailContext, response)
    
def renderHomePage(request: HttpRequest) -> HttpResponse:
    global EnterpriceName
    return render(request, 'index.html' , {"EnterpriceName": EnterpriceName})

def renderSendEmail(request: HttpRequest) -> HttpResponse:
    return render(request, 'get_email.html')

def saveEmail(clientEmail: str, text:str, response_message_relevant: bool, response_message_response: str) -> CheckedEmail:
    checked_email = CheckedEmail(
    clientEmail=clientEmail,
    emailMesage=text,
    relevence=response_message_relevant,
    response=response_message_response
    )
    checked_email.save()
    return checked_email


def receiveEmail(request: HttpRequest) -> HttpResponse:
    text = ""
    email = ""
    
    if request.method == "POST":
        email_id = request.POST.get('email_id')
        email = request.POST.get('email') 
        save = request.POST.get('save')
        if save:
            newresponse = request.POST.get('new_response')
            email_obj = get_object_or_404(CheckedEmail, id=email_id)
            email_obj.response = newresponse
            email_obj.save()
            return render(request, 'simple_response.html', {
                'text': email_obj.relevence,
                'dirt': email_obj.response,
                'sendBy': email_obj.clientEmail,
                'email_id': email_obj.id
            })

        if 'pdf_file' in request.FILES:
            pdf_file = request.FILES['pdf_file']
            reader = PdfReader(pdf_file)
            for page in reader.pages:
                text += page.extract_text() or ""

        elif 'txt_file' in request.FILES:
            txt_file = request.FILES['txt_file']
            text = txt_file.read().decode('utf-8')

        elif 'content' in request.POST:
            text = request.POST.get('content', '')
        if text:
            responseMensage = ProcessMensage(email, text)
            savedEmail = saveEmail(email, text, responseMensage.relevant, responseMensage.response)
            return render(request, 'simple_response.html', {
                'text': responseMensage.relevant,
                'dirt': responseMensage.response,
                'sendBy': email,
                'email_id': savedEmail.id
            })

    return render(request, 'simple_response.html')


def renderAllEmails(request: HttpRequest) -> HttpResponse:
    all_emails = CheckedEmail.objects.all().order_by('-clientEmail') 

    context = {
        'emails': all_emails
    }
    return render(request, 'render_emails.html', context)

def dropDataset(request: HttpRequest)-> HttpResponse:
    CheckedEmail.objects.all().delete()
    return redirect('home_page')

def sendEmail(request: HttpRequest)-> HttpResponse:
    dirt = request.GET.get('dirt')
    sendBy = request.GET.get('sendBy')
    subject = generateSubject(dirt)
    sendedEmail = se(subject, dirt, sendBy)
    return render(request, 'send_email_ok.html',{"sendE":sendedEmail})

def deleteEmail(request: HttpRequest, email_id) -> HttpResponse:
    email = get_object_or_404(CheckedEmail, id=email_id)
    email.delete()
    return redirect('read_email')

def editEmail(request: HttpRequest, email_id) -> HttpResponse:
    email_obj = get_object_or_404(CheckedEmail, id=email_id)
    return render(request, 'edit_email.html', {'email': email_obj})
