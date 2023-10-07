from django.shortcuts import render, redirect
from materiais.models import (
    Questao,
    Materia,
    Conteudo,
    ProvaCompleta,
    ProvaRespondida,
    Simulado,
    QuestaoRespondida,
)
from django.contrib import messages
from provas.forms import ProvaChoose
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from usuarios.decorators import user_has_tag
from django.http import HttpResponse
from usuarios.models import Aluno
from .funcs_geracao_prova import geracao_simulado, geracao_prova
from django.urls import reverse
# Create your views here.
@login_required
def prova_choose(request):
    if request.method == "POST":
        choose_prova = ProvaChoose(request.POST)

        if choose_prova.is_valid():
            tipo_prova = choose_prova.cleaned_data["tipo_prova"]
            request.session["tipo_prova"] = tipo_prova
            aluno = request.user.aluno

            if tipo_prova == "materia_escolhida":
                num_questoes = int(choose_prova.cleaned_data["num_questoes_prova"])
                materia_id_list = choose_prova.cleaned_data["materias"]
                if materia_id_list is None:
                    messages.add_message(request, messages.ERROR, f"{request.user.nome} Por favor escolha uma materia!")
                    return redirect(reverse("provas:prova-choose"))
                questoes, materias = geracao_prova(materia_id_list, num_questoes)

                context = {
                    "questoes": questoes,
                    "materias": materias,
                }
                return render(request, "provas/prova.html", context)

            if tipo_prova == "simulado":
                simulado_id_list = choose_prova.cleaned_data["simulados"]
                num_questoes = int(choose_prova.cleaned_data["num_questoes_simulado"])
                request.session["simulado_id_list"] = simulado_id_list
                print(f"simulado_id_list: {simulado_id_list}")
                if len(simulado_id_list) == 0:
                    messages.add_message(request, messages.ERROR, f"{request.user.nome}, por favor escolha uma matéria!")
                    return redirect(reverse("provas:prova-choose"))

                questoes, simulados = geracao_simulado(simulado_id_list, num_questoes, aluno)
                
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
@user_has_tag("is_aluno")
def prova_respondida(request):
    if request.method == "POST":        

        tipo_prova = request.session.get("tipo_prova")
        aluno = Aluno.objects.get(usuario=request.user)

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
            cache.delete(f"aluno_provas_feitas_{aluno.id}")
            cache.delete(f"turmas_graph_{aluno.id}")
            return render(request, "provas/prova-respondida.html", context)
        

        if tipo_prova == "simulado":
            simulado_id_list = request.session.get("simulado_id_list")
            simulados = Simulado.objects.filter(pk__in=simulado_id_list)
            for simulado in simulados:
                prova_completa = ProvaCompleta.objects.create(aluno=aluno, simulado=simulado)
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

                prova_completa.simulado = prova_respondida_obj.simulado

                # Deactivated QuestaoRespondida for DEV
                #questao_respondida = QuestaoRespondida()
                #questao_respondida.set_questoes_ja_respondidas(aluno)
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
    context = {
        "ranking_piores": ranking_piores,
        "ranking_melhores": ranking_melhores,
        "erros": erros,
        "acertos": acertos,
        "data": data,
    }

    return render(request, "provas/prova-completa.html", context)


@login_required
@user_has_tag("is_professor")
def criar_prova_professor(request):
    cache_key = f"criar_prova_professor"
    cached_page = cache.get(cache_key)
    
    if cached_page:
        return HttpResponse(cached_page)

    materias = Materia.objects.all().prefetch_related("sub_materia__conteudo__questoes")
    materias_data = []
    for materia in materias:
        materias_dict = {"nome": materia.nome, "sub_materias": []}
        for sub_materia in materia.sub_materia.all():
            sub_materia_dict = {
                "nome": sub_materia.nome,
                "conteudos": [],
            }
            for conteudo in sub_materia.conteudo.all():
                conteudo_dict = {
                    "nome": conteudo.nome,
                    "questoes": set(conteudo.questoes.all()),
                }
                sub_materia_dict["conteudos"].append(conteudo_dict)
            materias_dict["sub_materias"].append(sub_materia_dict)
        materias_data.append(materias_dict)

    context = {
        "materias_data": materias_data,
    }
    response = render(request, "provas/criacao-prova-professor.html", context)
    cache.set(cache_key, response.content, 60 * 10)
    return response
