from django.urls import path
from usuarios.views import user_view


app_name = 'usuarios'

urlpatterns = [
    path('', user_view, name='user'),
]
    
