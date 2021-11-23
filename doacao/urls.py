from django.urls import path

from .views import BaseView, UsuarioCreate, InstituicaoCreate, UsuarioDelete, Usuariolist, InstituicaoDelete, Instituicaolist, Produtolist, ProdutoCreate


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
]