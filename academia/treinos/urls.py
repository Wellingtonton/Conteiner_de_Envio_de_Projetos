from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_treinos, name='treinos'),
    path('novo/', views.novo_treino, name='novo_treino'),
    path('<int:id>/', views.detalhes_treino, name='detalhes_treino'),
]