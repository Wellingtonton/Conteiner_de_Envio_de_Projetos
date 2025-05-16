from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_fichas, name='lista_fichas'),
    path('nova/', views.nova_ficha, name='nova_ficha'),
    path('<int:id>/', views.detalhes_ficha, name='detalhes_ficha'),
]