from math import floor
from usuarios.funcs import filtra_questoes_feitas
from materiais.models import Conteudo, Questao, SubMateria


def retorna_questoes_unicas(
    questoes: list, num_questoes: int, questoes_da_materia, questoes_unicas: set
) -> list:
    """Nao deixa questoes serem repetidas em qualquer prova e as adciona na table de questoes feitas pelo usuario"""
    
    for questao in questoes_da_materia:
        if len(questoes) >= num_questoes:
            break
        if questao.id not in questoes_unicas:
            questoes.append(questao)
            questoes_unicas.add(questao.id)
    return questoes


def filtra_questoes_simulado_linguagens(
    num_questoes: int, materia_in_simulado, questoes: list, user, questoes_unicas: set
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
            questoes, num_questoes, questoes_da_materia, questoes_unicas
        )
        
    return questoes


def filtra_questoes_simulado_natureza(
    num_questoes: int, materia_in_simulado, questoes: list, user, questoes_unicas: set
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
    num_questoes: int, materia_in_simulado, questoes: list, user, questoes_unicas: set
) -> list:
    sub_materias_da_materia = SubMateria.objects.filter(materia=materia_in_simulado[0])
    conteudos = Conteudo.objects.filter(sub_materia__in=sub_materias_da_materia)
    questoes_da_materia = Questao.objects.filter(conteudo__in=conteudos).order_by("?")

    questoes = retorna_questoes_unicas(
        questoes, num_questoes, questoes_da_materia, questoes_unicas
    )


    return questoes
