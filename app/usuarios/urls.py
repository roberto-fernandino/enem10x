from django.urls import path
from usuarios.views import notas_graph, signup, signupsucess, logout_view, login_view, filter_graph_time


app_name = 'usuarios'

urlpatterns = [
    path('usuario/', notas_graph, name='user'),
    path('usuario/filter-graph-time/', filter_graph_time, name='graph-filter'),
    path('login/', login_view, name='login'),
    path('signup/', signup, name="signup"),
    path('conta-criada/', signupsucess, name='signup-sucess'),
    path('logout/', logout_view, name='logout'),
]
    
