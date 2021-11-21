from django.db.models import fields
from django.shortcuts import render, redirect
from .models import Usuario, Instituicao
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
class UsuarioCreate(CreateView):
   model = Usuario
   fields = ['nome', 'email']
   template_name = 'usuarios.html'
   sucess_url = reverse_lazy('base')

class InstituicaoCreate(CreateView):
   model = Instituicao
   fields = ['nome', 'email', 'endereco']
   template_name = 'instituicoes.html'
   sucess_url = reverse_lazy('base')

def inicio(request):
 return render(request, 'base.html')

#def cadastrar_usuarios(request):
 # return render(request, 'usuarios.html')

#def cadastrar_instituicoes(request):
 # return render(request, 'instituicoes.html')

#def produtos(request):
# return render(request, 'produtos.html')