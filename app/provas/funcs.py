from math import floor
from materiais.models import Conteudo, Questao, SubMateria, Materia, QuestaoRespondida
from usuarios.models import Aluno
import os


def retorna_questoes_unicas(
    aluno: Aluno
) -> list:
    """Nao deixa questoes serem repetidas em qualquer prova filtrando tambem pela table QuestaoRespondida
    onde aluno=aluno e adiciona retorna questoes_unicas"""
    
    questoes_unicas = (QuestaoRespondida.objects.filter(aluno=aluno).values_list("questao_id", flat=True)) # Pega todas as questoes ja respondidas 
    return questoes_unicas


def filtra_questoes_simulado_linguagens(
    num_questoes: int, materia_in_simulado, questoes: list, questoes_unicas: set, aluno: Aluno
) -> list:
    """
    Esse algoritimo maluco arrendoda via porcentagem o numero de questoes por materias especificadas em
    questoes_por_materia e caso haja discrepancias no total de num_questoesescolhidas pelo usuario
    ele pega a discrepancia e remove/adciona em portugues pra manter num_questoes sempre na linha.
    """
    questoes_por_materia = {
        "Educação Física": floor(0.08 * num_questoes),
        "Inglês": floor(0.13 * num_questoes),
        "Literatura": floor(0.13 * num_questoes),
        "Português": floor(0.66 * num_questoes),
    }
    total_questoes = sum(questoes_por_materia.values())
    discrepancia = num_questoes - total_questoes
    questoes_por_materia["Português"] += discrepancia
    for materia in materia_in_simulado:
        sub_materias_da_materia = SubMateria.objects.filter(materia=materia)
        conteudos = Conteudo.objects.filter(sub_materia__in=sub_materias_da_materia)
        questoes_da_materia = Questao.objects.filter(conteudo__in=conteudos).order_by(
            "?"
        )
        questoes = retorna_questoes_unicas(
            questoes, num_questoes, questoes_da_materia, aluno, questoes_unicas
        )

    return questoes


def filtra_questoes_simulado_natureza(
    num_questoes: int, materia_in_simulado, questoes: list, questoes_unicas: set, aluno: Aluno
) -> list:
    """
    Tenta dividir o numero de questoes escolhidas pelo usuario pelo numero de materias no simulado
    no caso 3. Caso o numero nao seja inteiro ele calcula a discrepancia e adicona/remove em biologia pois,
    biologia tem uma maior porcentagem nas questoes do enem oficiais.
    """

    questoes_por_materia = num_questoes // len(materia_in_simulado)
    total_questoes = questoes_por_materia * len(materia_in_simulado)
    discrepancia = num_questoes - total_questoes

    for materia in materia_in_simulado:
        sub_materias_da_materia = SubMateria.objects.filter(materia=materia)
        conteudos = Conteudo.objects.filter(sub_materia__in=sub_materias_da_materia)
        questoes_da_materia = Questao.objects.filter(conteudo__in=conteudos).order_by(
            "?"
        )
        questoes = retorna_questoes_unicas(
            questoes, num_questoes, questoes_da_materia, questoes_unicas
        )
        if materia.nome == "Biologia" and (discrepancia > 0 or discrepancia < 0):
            questoes_a_adcionar = questoes_por_materia + discrepancia
        else:
            questoes_a_adcionar = questoes_por_materia

    return questoes


def filtra_questoes_simulado_matematica(
    num_questoes: int, materia_in_simulado, questoes_unicas: set, aluno: Aluno
) -> list:
    """Faz a mesma coisa que as outras funcoes desse arquivo porem como a prova de matematica so tem\n
    matematica como materia eh mais simplificada."""

    questoes_unicas.update(retorna_questoes_unicas(aluno))
    questoes_ids = Questao.objects.filter(
        conteudo__sub_materia__materia=materia_in_simulado[0]
    ).exclude(id__in=questoes_unicas).values_list("id", flat=True).order_by("?")[:num_questoes]
    
    questoes_list = list(Questao.objects.filter(id__in=questoes_ids))
    

    return questoes_list

