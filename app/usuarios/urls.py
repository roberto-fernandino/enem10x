from django.urls import path
from usuarios.views import notas_graph, signup, signupsucess, logout_view, login_view, filter_graph_time, user_view, professor_turmas_view, criar_turma_view, professor_turma_view, entra_turma, delete_turma, aluno_turma_view, aluno_turmas_view, remover_aluno, sair_turma_aluno


app_name = 'usuarios'

urlpatterns = [
    path('plataforma/', user_view, name='user'),
    path('plataforma/graph', notas_graph, name='graficos'),
    path('plataforma/filter-graph-time/', filter_graph_time, name='graph-filter'),
    path('plataforma/professor/turmas/', professor_turmas_view, name='professor-turmas'),
    path('plataforma/aluno/turmas/', aluno_turmas_view, name='aluno-turmas'),
    path('plataforma/professor/criar-turmas/', criar_turma_view, name='criar-turma'),
    path('plataforma/professor/turma/<int:turma_id>', professor_turma_view, name='professor-turma'),
    path('plataforma/professor/turma/remover-aluno/<int:turma_id>/<int:aluno_id>', remover_aluno, name='remover-aluno'),
    path('plataforma/aluno/turma/<int:turma_id>', aluno_turma_view, name='aluno-turma'),
    path('plataforma/turma/delete/<int:turma_id>', delete_turma, name='delete-turma'),
    path('plataforma/turma/entrar/', entra_turma , name='entrar-turma'),
    path('plataforma/aluno/turma/sair/<int:turma_id>/<int:aluno_id>', sair_turma_aluno , name='aluno-sair-turma'),
    path('login/', login_view, name='login'),
    path('signup/', signup, name="signup"),
    path('conta-criada/', signupsucess, name='signup-sucess'),
    path('logout/', logout_view, name='logout'),
]
    
