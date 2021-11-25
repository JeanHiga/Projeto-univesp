from django.urls import path

from .views import BaseView, EntregaList, InicioView, SobreView, UsuarioCreate, InstituicaoCreate, UsuarioDelete, Usuariolist, InstituicaoDelete, Instituicaolist, Produtolist, ProdutoCreate,DoadorCreate



urlpatterns = [
    path('', BaseView.as_view(), name='base'),
#
    path('cadastrar/usuario/', UsuarioCreate.as_view(), name="cadastrar-usuario"),
    path('excluir/usuario/<int:pk>/', UsuarioDelete.as_view(), name="deletar-usuario"),
    path('listar/usuario/', Usuariolist.as_view(), name="listar-usuario"),
#
    path('cadastrar/instituicao/', InstituicaoCreate.as_view(),name="cadastrar-instituicao"),
    path('excluir/instituicao/<int:pk>/', InstituicaoDelete.as_view(), name="deletar-instituicao"),
    path('listar/instituicao/', Instituicaolist.as_view(), name="listar-instituicao"),

    path('cadastrar/produto/', ProdutoCreate.as_view(),name="cadastrar-produto"),
    path('listar/pedido/', Produtolist.as_view(), name="listar-pedido"),

    path('confirmar/doacao/', DoadorCreate.as_view(), name="confirmar-doacao"),
    path('confirmar/entrega/', EntregaList.as_view(), name="confirmar-entrega"),

    path('inicio', InicioView.as_view(), name='inicio'),
    path('sobre', SobreView.as_view(), name='sobre'),

]