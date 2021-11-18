from django.shortcuts import render, redirect
from .models import Usuario


# Create your views here.
def cadastrar_usuarios(request):
   return render(request, 'usuarios.html')

def cadastrar_instituicoes(request):
   return render(request, 'instituicoes.html')

def produtos(request):
   return render(request, 'produtos.html')