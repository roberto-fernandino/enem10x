from django.urls import path
from provas.views import prova_choose, prova_respondida, prova_completa,  criar_prova_professor

# App name for refering in other code parts
app_name = 'provas'

# Urls 
urlpatterns = [
    path('', prova_choose, name='prova-choose'),
    path('respondida/', prova_respondida, name='prova-respondida'),
    path('completa/<int:prova_id>/', prova_completa, name='prova-completa'),
    path('criar/', criar_prova_professor, name='criar-prova-professor'),
]