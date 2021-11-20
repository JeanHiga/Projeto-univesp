from django.urls import path

from .views import UsuarioCreate


urlpatterns = [
    path('cadastrar/usuario/', UsuarioCreate.as_view(), name="cadastrar-usuario"),
    
    #path('usuarios', cadastrar_usuarios, name='cadastrar_usuarios'),
    #path('instituicoes', cadastrar_instituicoes, name='cadastrar_instituicoes'),
    #path('produtos', produtos, name='produtos'),
    #path('', inicio, name='inicio'),

]