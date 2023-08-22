from django.shortcuts import render
from materiais.models import Questao, Materia

# Create your views here.
def prova_mat_view(request):
    materia = Materia.objects.get(nome="Matematica")
    questoes_selecionadas = []
    
    context = {}
    return render(request, 'materiais/prova.html', context)
