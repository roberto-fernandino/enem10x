from django.urls import path
from usuarios.views import user_view, signup, signupsucess, logout_view, login_view


app_name = 'usuarios'

urlpatterns = [
    path('usuario/', user_view, name='user'),
    path('login/', login_view, name='login'),
    path('signup/', signup, name="signup"),
    path('conta-criada/', signupsucess, name='signup-sucess'),
    path('logout/', logout_view, name='logout'),
]
    
