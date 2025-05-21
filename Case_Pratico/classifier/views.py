from django.shortcuts import render
from django.http import HttpResponse

class ProcessedEmail:
    personName: str
    relevant: bool
    email: str


def iaProcess(email: str) -> str:
    #TODO make the ia process to classifier the email
    pass

def EmailReader(request: HttpResponse):
    if request.method == "POST":
        email = request.POST.get('email')
        personName = request.POST.get('name')
        iaProcess(email, personName)

