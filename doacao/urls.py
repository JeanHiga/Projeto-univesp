from django.urls import path

from .views import BaseView, UsuarioCreate, InstituicaoCreate, UsuarioDelete, Usuariolist



urlpatterns = [
    path('', BaseView.as_view(), name='base'),
    path('cadastrar/usuario/', UsuarioCreate.as_view(), name="cadastrar-usuario"),
    path('excluir/usuario/<int:pk>/', UsuarioDelete.as_view(), name="deletar-usuario"),
    path('listar/usuario/', Usuariolist.as_view(), name="listar-usuario"),
    path('cadastrar/instituicao/', InstituicaoCreate.as_view(),name="cadastrar-instituicao"),

    

]