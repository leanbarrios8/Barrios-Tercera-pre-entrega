from django.urls import path
from bitcoin import views

urlpatterns = [
    path('', views.bitcoin, name="bitcoin"),
]