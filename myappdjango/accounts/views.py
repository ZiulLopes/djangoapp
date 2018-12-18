from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):

    programing_languages = ['python', '.net', 'android', 'swift', 'asp', 'javascript', 'java']
    name = 'Luiz Fernando lopes'
    args = {'name': name, 'programing_languages': programing_languages}

    return render(request, "accounts/home.html", args)

def login(request):
    return render(request, "accounts/login.html")