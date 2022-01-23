# THIS FILE CREATED BY ABEER ALI KHAN
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to my homepage")

def aboutMe(request):
    return HttpResponse("<b>Abeer Ali Khan is a mastermind!</b>")

def notes(request):
    with open('../notes.txt', 'r') as file:
        file = file.read()
        return HttpResponse(file)