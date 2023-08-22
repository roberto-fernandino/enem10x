from django.urls import path
from materiais.views import prova_mat_view
# urls aqui

app_name = 'materiais'

urlpatterns = [
    path('prova-mat', prova_mat_view, name='prova-mat')
]