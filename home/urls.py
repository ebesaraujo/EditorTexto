from django.urls import path, include
from home import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('home/salvar', views.salvar, name='salvar'),
]