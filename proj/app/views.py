from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Página Inicial</h1>")

def about(request):
    return HttpResponse("<h1>Sobre o Projeto</h1>")

def contact(request):
    return HttpResponse("<h1>Contatos</h1>")
