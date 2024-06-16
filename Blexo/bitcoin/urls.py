from django.urls import path
from . import views

urlpatterns = [
    path('', views.bitcoin, name='bitcoin'),
    path('lista/', views.lista, name='lista'),
    path('monedas/', views.monedas, name='monedas'),
]