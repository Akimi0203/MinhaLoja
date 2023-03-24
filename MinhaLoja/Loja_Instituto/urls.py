from django.urls import path
from . import views

urlpatterns = [
    # path('cadastro/', views.cadastro, name='cadastro'),
    # path('acesso/', views.acesso, name='acesso'),
    path('cliente/', views.cliente, name='cliente'),
    path('produto/', views.produto, name='produto'),
    path('salvar/', views.salvar, name='salvar'),
    # path('ler/', views.ler, name='ler'),
    # path('lista/', views.lista, name='lista'),
    path('', views.raiz, name='raiz'),
]