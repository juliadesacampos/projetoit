from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"app_aula/index.html")

def autor(request):
    return render(request,"app_aula/autor.html")

def personagem(request):
    return render(request,"app_aula/personagem.html")