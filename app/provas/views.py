from django.shortcuts import render
from materiais.models import (
    Questao,
    Materia,
    SubMateria,
    Conteudo,
    ProvaCompleta,
    ProvaRespondida,
    Nivel,
    Simulado,
    QuestaoRespondida,
)
from provas.forms import ProvaChoose
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from math import floor
from provas.funcs import (
    filtra_questoes_simulado_linguagens,
    filtra_questoes_simulado_natureza,
    filtra_questoes_simulado_matematica,
)
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from usuarios.decorators import user_has_tag

# Create your views here.
@login_required
def prova_choose(request):
    if request.method == "POST":
        choose_prova = ProvaChoose(request.POST)
        if choose_prova.is_valid():
            print("valid")
            tipo_prova = choose_prova.cleaned_data["tipo_prova"]
            num_questoes = int(choose_prova.cleaned_data["num_questoes"])
            request.session["tipo_prova"] = tipo_prova

            if tipo_prova == "materia_escolhida":
                # Recebe id de materias e simulados
                materia_id_list = choose_prova.cleaned_data["materias"]
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
                    questoes_da_materia = Questao.objects.filter(
                        conteudo__in=conteudos
                    ).order_by("?")
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

            if tipo_prova == "simulado":
                simulado_id_list = choose_prova.cleaned_data["simulados"]              
                request.session["simulado_id_list"] = simulado_id_list                
                simulados = Simulado.objects.filter(pk__in=simulado_id_list)
                questoes = []
                questoes_unicas = set()
                for simulado in simulados:
                    # Materia de cada simulado
                    materia_in_simulado = simulado.materia.all()
                    # Se um simulado for de matematica a quantidade de questoes do simulado sera 100% matematica como no enem
                    if (
                        len(materia_in_simulado) == 1
                        and materia_in_simulado[0].nome == "Matemática"
                    ):
                        questoes = filtra_questoes_simulado_matematica(
                            num_questoes,
                            materia_in_simulado,
                            questoes,
                            questoes_unicas,
                        )
                    # Se um dos simulados for de ciencias da natureza
                    if len(materia_in_simulado) == 3:
                        questoes = filtra_questoes_simulado_natureza(
                            num_questoes,
                            materia_in_simulado,
                            questoes,
                            questoes_unicas,
                        )
                    # Se um dos simulados for de Linguagens
                    if len(materia_in_simulado) == 5:
                        filtra_questoes_simulado_linguagens(
                            num_questoes,
                            materia_in_simulado,
                            questoes,
                            questoes_unicas,
                        )
                context = {
                    "questoes": questoes,
                    "simulados": simulados,
                }               
                return render(request, "provas/prova.html", context)
    choose_prova = ProvaChoose()
    context = {
        "choose_prova": choose_prova,
    }
    return render(request, "provas/escolha-prova.html", context)

@login_required
@user_has_tag('is_aluno')
def prova_respondida(request):
    if request.method == "POST":
        tipo_prova = request.session.get("tipo_prova")
        aluno = request.user.aluno
        # se a prova for materia_escolhida
        if tipo_prova == "materia_escolhida":
            prova_completa = ProvaCompleta.objects.create(aluno=aluno)
            for questao_id, resposta in request.POST.items():
                if "questao_id-" in questao_id:
                    real_questao_id = questao_id.split("-")[1]
                    questao = Questao.objects.get(id=real_questao_id)
                    prova_respondida_obj = ProvaRespondida.objects.create(
                        aluno=aluno,
                        questao=questao,
                        resposta=resposta,
                        prova_completa=prova_completa,
                    )
                    # Define acerto da questao
                    prova_respondida_obj.set_acerto()
            questao_respondida = QuestaoRespondida()
            questao_respondida.set_questoes_ja_respondidas(aluno)
            prova_completa.gera_relatorio()
            # Deleta as questoes respondidas do usuario para nao poluir o banco de dados com informacao inutil.
            prova_completa.deleta_respostas()
            prova_completa_url = reverse(
                "provas:prova-completa", args=[prova_completa.id]
            )
            context = {"prova_completa_url": prova_completa_url}
            cache.delete(f"aluno")
            return render(request, "provas/prova-respondida.html", context)
        # se a prova for simulado
        if tipo_prova == "simulado":
            simulado_id_list = request.session.get("simulado_id_list")
            simulados = Simulado.objects.filter(pk__in=simulado_id_list)
            for simulado in simulados:
                prova_completa = ProvaCompleta.objects.create(aluno=aluno)
                for questao_id, resposta in request.POST.items():
                    if "questao_id-" in questao_id:
                        real_questao_id = questao_id.split("-")[1]
                        questao = Questao.objects.get(pk=real_questao_id)
                        prova_respondida_obj = ProvaRespondida.objects.create(
                            aluno=aluno,
                            questao=questao,
                            resposta=resposta,
                            prova_completa=prova_completa,
                            simulado=simulado,
                        )
                        prova_respondida_obj.set_acerto()
                questao_respondida = QuestaoRespondida()
                questao_respondida.set_questoes_ja_respondidas(aluno)
                prova_completa.gera_relatorio()
                prova_completa.deleta_respostas()
                prova_completa_url = reverse(
                    "provas:prova-completa", args=[prova_completa.id]
                )
                context = {"prova_completa_url": prova_completa_url}
                cache.delete(f"aluno_provas_feitas_{aluno.id}")
                cache.delete(f"turmas_graph_{aluno.id}")
            return render(request, "provas/prova-respondida.html", context)


def prova_completa(request, prova_id):
    prova_completa_obj = ProvaCompleta.objects.get(pk=prova_id)
    ranking_piores = {
        Conteudo.objects.get(pk=conteudo_id).nome: quantidade
        for conteudo_id, quantidade in sorted(
            prova_completa_obj.ranking_piores_conteudos.items(),
            key=lambda x: x[1],
            reverse=True,
        )
    }
    ranking_melhores = {
        Conteudo.objects.get(pk=conteudo_id).nome: quantidade
        for conteudo_id, quantidade in sorted(
            prova_completa_obj.ranking_melhores_conteudos.items(),
            key=lambda x: x[1],
            reverse=True,
        )
    }
    acertos = prova_completa_obj.acertos
    erros = prova_completa_obj.erros
    data = prova_completa_obj.data_feita
    acerto_dificuldade = {
        Nivel.objects.get(pk=nivel_id).nivel: quantidade
        for nivel_id, quantidade in prova_completa_obj.acerto_dificuldade.items()
    }
    context = {
        "ranking_piores": ranking_piores,
        "ranking_melhores": ranking_melhores,
        "erros": erros,
        "acertos": acertos,
        "data": data,
        "acerto_dificuldade": acerto_dificuldade,
    }
    
    return render(request, "provas/prova-completa.html", context)



