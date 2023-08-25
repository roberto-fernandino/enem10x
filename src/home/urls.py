from django.urls import path
from home.views import home_view

# App name for refering in other code parts
app_name = 'home'

# Urls 
urlpatterns = [
    path('', home_view, name='home')
]