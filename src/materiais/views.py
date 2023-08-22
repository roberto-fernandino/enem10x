from django.shortcuts import render
from materiais.models import Questao, Materia


# Create your views here.
def prova_mat_view(request):
    questoes = Questao.objects.all()
    context = {"questoes": questoes}
    return render(request, "materiais/prova.html", context)
