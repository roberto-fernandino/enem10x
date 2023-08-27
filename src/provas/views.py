from django.shortcuts import render
from materiais.models import Questao, Materia, SubMateria, Conteudo, ProvaCompleta, ProvaRespondida, Nivel
from provas.forms import ProvaChoose
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.
@login_required
def prova(request):
    if request.method == "POST":
        choose_prova = ProvaChoose(request.POST)
        if choose_prova.is_valid():
            # Recebe id de materias
            materia_id_list = choose_prova.cleaned_data["materias"]
            # Recebe numero de questoes de cada materia que deseja
            num_questoes = int(choose_prova.cleaned_data["num_questoes"])
            # Filtra materias pelo id e guarda numa lista de materias
            materias = Materia.objects.filter(pk__in=materia_id_list)
            questoes = []
            questoes_unicas = set()

            # Pega o n de questoes escolhido de cada materia escolhida
            for materia in materias:
                sub_materias_da_materia = SubMateria.objects.filter(materia=materia)
                conteudos = Conteudo.objects.filter(
                    sub_materia__in=sub_materias_da_materia
                )
                questoes_da_materia = Questao.objects.filter(conteudo__in=conteudos).order_by("?")
                questoes_selecionadas = 0
                for questao in questoes_da_materia:
                    if questoes_selecionadas >= num_questoes:
                        break
                    if questao.id not in questoes_unicas:
                        questoes_unicas.add(questao.id)
                        questoes.append(questao)
                        questoes_selecionadas += 1

            context = {
                "questoes": questoes,
                "materias": materias,
            }
        return render(request, "provas/prova.html", context)

    choose_prova = ProvaChoose()

    context = {
        "choose_prova": choose_prova,
    }

    return render(request, "provas/escolha-prova.html", context)


def prova_respondida(request):
    if request.method == "POST":
        prova_completa = ProvaCompleta.objects.create(usuario=request.user)
        for questao_id, resposta in request.POST.items():
            if 'questao_id-' in questao_id:
                real_questao_id = questao_id.split('-')[1]
                questao = Questao.objects.get(id=real_questao_id)
                prova_respondida_obj = ProvaRespondida.objects.create(
                    usuario=request.user,
                    questao=questao,
                    resposta=resposta,
                    prova_completa= prova_completa
                    )
                # Define acerto da questao
                prova_respondida_obj.set_acerto()
        
        prova_completa.gera_relatorio()
        prova_completa.deleta_respostas()
        prova_completa_url = reverse('provas:prova-completa', args=[prova_completa.id])
        context = {
            'prova_completa_url': prova_completa_url
        }
        return render(request, "provas/prova-respondida.html", context)

def prova_completa(request, prova_id):
    prova_completa_obj = ProvaCompleta.objects.get(pk=prova_id)
    ranking_piores = {Conteudo.objects.get(pk=conteudo_id).nome: quantidade for conteudo_id, quantidade in sorted(prova_completa_obj.ranking_piores_conteudos.items(), key=lambda x: x[1], reverse=True)}
    ranking_melhores = {Conteudo.objects.get(pk=conteudo_id).nome: quantidade for conteudo_id, quantidade in sorted(prova_completa_obj.ranking_melhores_conteudos.items(), key=lambda x: x[1], reverse=True)}
    acertos = prova_completa_obj.acertos
    erros = prova_completa_obj.erros
    data = prova_completa_obj.data_feita
    acerto_dificuldade = {Nivel.objects.get(pk=nivel_id).nivel: quantidade for nivel_id, quantidade in prova_completa_obj.acerto_dificuldade.items()}
    context = {
        "ranking_piores": ranking_piores,
        "ranking_melhores": ranking_melhores,
        "erros": erros,
        "acertos": acertos,
        "data": data,
        "acerto_dificuldade": acerto_dificuldade,

    }
    return render(request, "provas/prova-completa.html", context)