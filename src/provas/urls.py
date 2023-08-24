from django.urls import path
from provas.views import prova

# App name for refering in other code parts
app_name = 'provas'

# Urls 
urlpatterns = [
    path('', prova, name='prova-mat')
]