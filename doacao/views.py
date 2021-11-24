from .models import Produto, Usuario, Instituicao,Doador

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from django.views.generic.list import ListView

from django.urls import reverse_lazy


# Create your views here.
class BaseView(TemplateView):
   template_name = 'base.html'

##########USUARIO##############
class UsuarioCreate(CreateView):
   model = Usuario
   fields = ['nome', 'email']
   template_name = 'form.html'
   success_url = reverse_lazy('base')

class UsuarioDelete(DeleteView):
   model = Usuario
   template_name = 'formdelete.html'
   success_url = reverse_lazy("listar-usuario")

class Usuariolist(ListView):
   model = Usuario
   template_name = 'listarusuario.html'
   
########Instituição################
class InstituicaoCreate(CreateView):
   model = Instituicao
   fields = ['nome', 'email', 'endereco']
   template_name = 'form.html'
   success_url = reverse_lazy("base")

class InstituicaoDelete(DeleteView):
   model = Instituicao
   template_name = 'formdelete.html'
   success_url = reverse_lazy("listar-instituicao")

class Instituicaolist(ListView):
   model = Instituicao
   template_name = 'listarinstituicao.html'



########Produtos#####################  

class Produtolist(ListView):
   model = Produto
   template_name = 'listarpedido.html'
   
class ProdutoCreate(CreateView):
   model = Produto
   fields = ['nome', 'quantidade', 'instituicao']
   template_name = 'form.html'
   success_url = reverse_lazy('base')


class DoadorCreate(CreateView):
   model = Doador
   fields = ['usuario', 'produto', 'instituicao']
   template_name = 'confirmardoacao.html'
   success_url = reverse_lazy('base')


