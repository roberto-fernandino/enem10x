from django.shortcuts import render
from materiais.models import Questao, Materia, SubMateria, Conteudo
from provas.forms import ProvaChoose
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def prova(request):
    if request.method == "POST":
        choose_prova = ProvaChoose(request.POST)
        if choose_prova.is_valid():
            materia_id_list = choose_prova.cleaned_data['materias']
            num_questoes = int(choose_prova.cleaned_data['num_questoes'])
            materias = Materia.objects.filter(pk__in=materia_id_list)
            sub_materias = SubMateria.objects.filter(materia__in=materias)
            conteudos = Conteudo.objects.filter(sub_materia__in=sub_materias)
            questoes = Questao.objects.filter(conteudo__in=conteudos)[:num_questoes]
            context = {
            "questoes": questoes,
            "materias": materias,
                   }
        return   render(request, "provas/prova.html", context)
    choose_prova = ProvaChoose()
    context = {
        "choose_prova": choose_prova,
        }
    return render(request, "provas/escolha-prova.html", context)

        