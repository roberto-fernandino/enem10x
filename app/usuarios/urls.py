from django.urls import path
from usuarios.views import notas_graph, signup, signupsucess, logout_view, login_view, filter_graph_time, user_view, turmas_view, criar_turma_view, turma_view


app_name = 'usuarios'

urlpatterns = [
    path('plataforma/', user_view, name='user'),
    path('plataforma/graph', notas_graph, name='graficos'),
    path('plataforma/filter-graph-time/', filter_graph_time, name='graph-filter'),
    path('plataforma/turmas/', turmas_view, name='turmas'),
    path('plataforma/criar-turmas/', criar_turma_view, name='criar-turma'),
    path('plataforma/turma/<int:turma_id>', turma_view, name='turma'),
    path('login/', login_view, name='login'),
    path('signup/', signup, name="signup"),
    path('conta-criada/', signupsucess, name='signup-sucess'),
    path('logout/', logout_view, name='logout'),
]
    
