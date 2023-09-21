from math import floor
from materiais.models import Conteudo, Questao, SubMateria, Materia, QuestaoRespondida
from usuarios.models import Aluno
import os


def retorna_questoes_unicas(
    aluno: Aluno
) -> list:
    """
    Retorna um conjunto de IDs de questões já respondidas pelo aluno.

    Esta função busca todas as questões que o aluno especificado já respondeu,
    para garantir que, ao gerar um novo conjunto de questões para o aluno, essas questões
    não sejam repetidas. Isso ajuda a manter a integridade do processo de avaliação e
    oferece ao aluno uma nova experiência em cada teste.

    Parameters:
    - aluno (Aluno): A instância do aluno para o qual as questões já respondidas estão sendo recuperadas.

    Returns:
    - list[int]: Uma lista de IDs das questões que o aluno já respondeu.

    Example:
    >>> retorna_questoes_unicas(aluno_obj)
    >>> [1, 23, 45, ...]
    """
    
    questoes_unicas = (QuestaoRespondida.objects.filter(aluno=aluno).values_list("questao_id", flat=True)) # Pega todas as questoes ja respondidas 
    return questoes_unicas


def filtra_questoes_simulado_linguagens(
    num_questoes: int, materia_in_simulado, questoes_unicas: set, aluno: Aluno
) -> list:
    """
    Esse algoritimo inicial maluco arrendoda via porcentagem o numero de questoes por materias especificadas em
    questoes_por_materia e caso haja discrepancias no total de num_questoesescolhidas pelo usuario
    ele pega a discrepancia e remove/adciona em portugues pra manter num_questoes sempre na linha.

    Documentacao: 
   
    Seleciona questões para o simulado com base em matérias de Linguagens.

    A função seleciona questões de acordo com uma distribuição predefinida entre as 
    sub-matérias de Linguagens. A matéria "Português" é ajustada para absorver discrepâncias 
    no total de questões. Questões já respondidas pelo aluno são excluídas.

    Parameters:
    - num_questoes (int): Total de questões desejadas no simulado.
    - materia_in_simulado (QuerySet): Materiais que fazem parte do simulado.
    - questoes_unicas (set): Conjunto de IDs de questões já selecionadas ou respondidas.
    - aluno (Aluno): Instância do aluno para o qual o simulado está sendo gerado.

    Returns:
    - list: Lista de questões selecionadas para o simulado.

    Example:
    
    >>> filtra_questoes_simulado_linguagens(45, [<Materia: Português>, <Materia: Inglês>], set(), aluno_obj)
    [<Questao: Questao1>, <Questao: Questao2>, ...,  <Questao: Questa45>]
    """

    
    questoes_por_materia = {
        "Educação Física": floor(0.08 * num_questoes),
        "Inglês": floor(0.13 * num_questoes),
        "Literatura": floor(0.13 * num_questoes),
        "Português": floor(0.66 * num_questoes),
    }
    total_questoes = sum(questoes_por_materia.values())
    discrepancia = num_questoes - total_questoes
    if discrepancia:
        questoes_por_materia["Português"] += discrepancia

    questoes_unicas.update(retorna_questoes_unicas(aluno))
    todos_questoes_objs = []
    for materia in materia_in_simulado:
        sub_materias_da_materia = SubMateria.objects.filter(materia=materia)
        conteudos = Conteudo.objects.filter(sub_materia__in=sub_materias_da_materia)
        questoes_da_materia_objs = Questao.objects.filter(conteudo__in=conteudos).exclude(id__in=questoes_unicas).order_by("?")[:questoes_por_materia[materia.nome]]
        todos_questoes_objs.extend(questoes_da_materia_objs)

    questoes_unicas.update(questao.id for questao in todos_questoes_objs)

    return  todos_questoes_objs


def filtra_questoes_simulado_natureza(
    num_questoes: int, materia_in_simulado, questoes_unicas: set, aluno: Aluno
) -> list:
    """
    Seleciona questões para o simulado com base em matérias de Ciências da Natureza.

    A função distribui as questões entre Biologia, Física e Química. Biologia recebe questões 
    adicionais em caso de discrepâncias na distribuição. Questões já respondidas pelo aluno são excluídas.

    Parameters:
    - num_questoes (int): Total de questões desejadas no simulado.
    - materia_in_simulado (QuerySet): Materiais que fazem parte do simulado.
    - questoes_unicas (set): Conjunto de IDs de questões já selecionadas.
    - aluno (Aluno): Instância do aluno para o qual o simulado está sendo gerado.

    Returns:
    - list: Lista de questões selecionadas para o simulado.

    Example:
    >>> filtra_questoes_simulado_natureza(15, materias, set(), aluno_obj)
    >>> [<Questao: Questao1>, <Questao: Questao2>, ...]
    """
    questoes_por_materia = {
        "Biologia": num_questoes // 3,
        "Física": num_questoes // 3,
        "Química":  num_questoes // 3
    }

    total_questoes = sum(questoes_por_materia.values())
    discrepancia = num_questoes - total_questoes
    if discrepancia:
        questoes_por_materia['Biologia'] += discrepancia

    questoes_unicas.update(retorna_questoes_unicas(aluno)) 
    todos_questoes_objs = []
    for materia in materia_in_simulado:
        sub_materias_da_materia = SubMateria.objects.filter(materia=materia) 
        conteudos = Conteudo.objects.filter(sub_materia__in=sub_materias_da_materia)# Futura funcao para pegar conteudos que o usuario mais precisa AQUI. 
        questoes_da_materia_objs = Questao.objects.filter(conteudo__in=conteudos).exclude(id__in=questoes_unicas).order_by("?")[:questoes_por_materia[materia.nome]]
        todos_questoes_objs.extend(questoes_da_materia_objs)

    questoes_unicas.update(questao.id for questao in todos_questoes_objs)

    return todos_questoes_objs


def filtra_questoes_simulado_matematica(
    num_questoes: int, materia_in_simulado, questoes_unicas: set, aluno: Aluno
) -> list:
    """
    Filtra e adiciona questões de Matemática ao conjunto de questões fornecido.
    
    Esta função seleciona questões de matemática para um simulado, baseando-se nas questões 
    ainda não respondidas pelo aluno. As questões selecionadas são então adicionadas ao conjunto 
    de questões fornecido (argumento `questoes`) e também são atualizadas no conjunto de questões únicas.
    
    Parameters:
    - num_questoes (int): Total de questões desejadas a serem adicionadas de Matemática.
    - materia_in_simulado (QuerySet): Matéria(s) que faz(em) parte do simulado.
    - questoes_unicas (set): Conjunto de IDs de questões já selecionadas ou respondidas.
    - aluno (Aluno): Instância do aluno para o qual o simulado está sendo gerado.
    
    Returns:
    - list: Lista questões para o simulado, incluindo as questões de Matemática selecionadas.
    
    Example:
    >>> questoes = []
    >>> filtra_questoes_simulado_matematica(questoes, 10, [<Materia: Matemática>], set(), aluno_obj)
    >>> [<Questao: Questao1>, <Questao: Questao2>, ... ,<Questao: Questao10>]
    """
    questoes_unicas.update(retorna_questoes_unicas(aluno))
    questoes_ids = Questao.objects.filter(
        conteudo__sub_materia__materia=materia_in_simulado[0]
    ).exclude(id__in=questoes_unicas).values_list("id", flat=True).order_by("?")[:num_questoes]
    todos_questoes_objs = list(Questao.objects.filter(id__in=questoes_ids))
    questoes_unicas.update(questao.id for questao in todos_questoes_objs)

    return todos_questoes_objs


def filtra_questoes_simulado_humanas(
        num_questoes:int, materia_in_simulado, questoes_unicas:set, aluno: Aluno
) -> list:
    questoes_unicas.update(retorna_questoes_unicas(aluno))
    questoes_por_materia = {

    }
