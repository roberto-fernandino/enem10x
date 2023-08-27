from django.urls import path
from provas.views import prova, prova_respondida, prova_completa

# App name for refering in other code parts
app_name = 'provas'

# Urls 
urlpatterns = [
    path('', prova, name='prova'),
    path('respondida/', prova_respondida, name='prova-respondida'),
    path('completa/<int:prova_id>/', prova_completa, name='prova-completa'),
]