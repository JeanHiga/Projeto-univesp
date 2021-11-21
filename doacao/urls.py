from django.urls import path

from .views import UsuarioCreate, InstituicaoCreate
from .views import inicio


urlpatterns = [
    path('cadastrar/usuario/', UsuarioCreate.as_view(), name="cadastrar-usuario"),
    path('cadastrar/instituicao/', InstituicaoCreate.as_view(), name="cadastrar-instituicao"),
    path('', inicio, name='inicio'),

]