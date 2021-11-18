from django.urls import path
from .views import cadastrar_usuarios
from .views import produtos
from .views import cadastrar_instituicoes

urlpatterns = [
    path('cadastrar/usuarios', cadastrar_usuarios, name='cadastrar_usuarios'),
    path('cadastrar/instituicoes', cadastrar_instituicoes, name='cadastrar_instituicoes'),
    path('produtos', produtos, name='produtos')

]