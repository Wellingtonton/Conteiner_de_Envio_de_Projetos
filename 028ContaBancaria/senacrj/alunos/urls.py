from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_alunos, name='lista_alunos'),
    path('novo/', views.novo_aluno, name='novo_aluno'),
    path('<int:id>/', views.detalhes_aluno, name='detalhes_aluno'),
]
