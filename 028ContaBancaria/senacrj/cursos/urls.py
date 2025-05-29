from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_cursos, name='lista_cursos'),
    path('novo/', views.novo_curso, name='novo_curso'),
    path('<int:id>/', views.detalhes_curso, name='detalhes_curso'),
]
