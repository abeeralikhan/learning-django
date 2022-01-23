# Created by Abeer Ali Khan
from django.http import HttpResponse

def index(request):
    return HttpResponse('''Welcome to my personal website navigator<br>
    Page 1: <a href='/github'>GitHub</a><br>
    Page 2: <a href='/linkedin'>Linkedin</a><br>
    Page 3: <a href='/google'>Google</a>''')

def google(request):
    return HttpResponse('''<a href='https://www.google.com'>Goto Google</a><br>
    <a href='/'>Back</a>''')

def github(request):
    return HttpResponse("<a href='https://www.github.com/abeeralikhan'>Goto my github profile</a>")

def linkedin(request):
    return HttpResponse("<a href='https://www.linkedin.com/in/abeeralikhan'>Goto my linkedin profile</a>")
