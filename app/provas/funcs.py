from math import floor
from materiais.models import Conteudo, Questao, SubMateria, Materia, QuestaoRespondida, GrupoConteudo
from usuarios.models import Aluno
import os
from random import sample, randint, choice

def retorna_questoes_unicas(aluno: Aluno) -> list:
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
    questoes_unicas = QuestaoRespondida.objects.filter(aluno=aluno).values_list(
        "questao_id", flat=True
    )  # Pega todas as questoes ja respondidas
    return questoes_unicas


def define_proporcao_conteudos_provas(materia_in_simulado:list, num_questoes:int):
    '''

        ## Descrição

        A função `define_proporcao_conteudos_provas` determina o número de questões que cada conteúdo deve ter em uma prova com base na proporção definida para cada grupo de conteúdo.

        ## Parâmetros

        - `materia_in_simulado` (`list`): Uma lista de objetos de matéria que estão no simulado.
        - `num_questoes` (`int`): O número total de questões na prova.

        ## Retorno

        Retorna um dicionário onde as chaves são os IDs dos conteúdos e os valores são o número de questões que cada conteúdo deve ter na prova.

        # Exemplo de uso

        ```python
        resultado = define_proporcao_conteudos_provas(materia_in_simulado, num_questoes)
        print(resultado)
        ```
        ### Output

        ```python
        {'2': 5, '7':10, '8':6,...}
        ``` 
        ### Onde: `id_conteudo`: num_questoes_por_conteudo
    '''
    conteudo_questoes_dict = {}
    soma_total_questoes_grupo = 0
    total_proporcao = (sum(grupo.proporcao for materia in materia_in_simulado for grupo in GrupoConteudo.objects.filter(materia=materia)))
    grupo_menor_qtd_questoes_id_qtd = [None, 45]
    for materia in materia_in_simulado:
        grupos_de_conteudos = GrupoConteudo.objects.filter(materia=materia).prefetch_related('conteudos')
                
        for grupo in grupos_de_conteudos:
            conteudos = list(grupo.conteudos.all()) # Recupera conteudos do grupo de conteudos

            total_questoes_grupo = round(num_questoes * (grupo.proporcao / total_proporcao)) # Total questoes que o grupo tera
            print(f"Grupo {grupo.id}: Total de questões do grupo: {total_questoes_grupo}")
            if total_questoes_grupo < grupo_menor_qtd_questoes_id_qtd[1]:
                grupo_menor_qtd_questoes_id_qtd = [grupo.id, total_questoes_grupo]

            soma_total_questoes_grupo += total_questoes_grupo 
            if total_questoes_grupo >= 1:
            
                if total_questoes_grupo == 1:
                    conteudo = choice(conteudos)
                    conteudo_questoes_dict[conteudo.id] = 1
            
                else:
                    num_conteudos_por_grupo = randint(1, len(conteudos)) 
                    conteudos_escolhidos = sample(list(conteudos), num_conteudos_por_grupo)
                    questoes_por_contuedo = total_questoes_grupo // num_conteudos_por_grupo
                    discrepancia = total_questoes_grupo - (len(conteudos_escolhidos) * questoes_por_contuedo)
                    print(f"Discrepancia no grupo: {discrepancia} Total questoes Grupo : {total_questoes_grupo}")
                    for conteudo in conteudos_escolhidos:
                        conteudo_questoes_dict[f"{conteudo.id}"] = questoes_por_contuedo
                        for _ in range(discrepancia):
                            if discrepancia:
                                conteudo = choice(list(conteudos_escolhidos))
                                if f'{conteudo.id}' not in conteudo_questoes_dict:
                                    conteudo_questoes_dict[f'{conteudo.id}'] = 0
                                conteudo_questoes_dict[f'{conteudo.id}'] += 1
                                discrepancia -= 1
                        print(conteudo_questoes_dict)
            else:   
                print(f"o grupo {grupo.id}: {grupo} resultou em 0 questoes. Total_questoes_grupo {total_questoes_grupo} ")
    soma_real_questoes = sum(conteudo_questoes_dict.values())
    discrepancia = num_questoes - soma_real_questoes
    print(f'Soma real questoes: {soma_real_questoes}')
    print(f'Discrepancia final: {discrepancia}')
    if discrepancia:
        grupo = GrupoConteudo.objects.filter(id=grupo_menor_qtd_questoes_id_qtd[0]).prefetch_related('conteudos').first()
        conteudos = list(grupo.conteudos.all())
        num_conteudos_por_grupo = randint(1, len(conteudos))
        conteudos_escolhidos = sample(list(conteudos), num_conteudos_por_grupo)
        while discrepancia:
            discrepancia -= 1
            conteudo = choice(conteudos_escolhidos)
            if f'{conteudo.id}' not in conteudo_questoes_dict:
                conteudo_questoes_dict[f"{conteudo.id}"] = 0
            conteudo_questoes_dict[f"{conteudo.id}"] += 1
    print(f'Questoes finais: {sum(conteudo_questoes_dict.values())}')
    return conteudo_questoes_dict


def filtra_questoes_simulado_linguagens(
    num_questoes: int, materia_in_simulado, questoes_unicas: set, aluno: Aluno
) -> list:
    """
    Esse algoritimo inicial maluco arrendoda via porcentagem o numero de questoes por materias especificadas em
    questoes_por_materia e caso haja discrepancias no total de num_questoesescolhidas pelo usuario
    ele pega a discrepancia e remove/adciona em portugues pra manter num_questoes sempre na linha.

    

    # Seleciona questões para o simulado com base em matérias de Linguagens.

    A função seleciona questões de acordo com uma distribuição predefinida entre as
    sub-matérias de Linguagens. A matéria "Português" é ajustada para absorver discrepâncias
    no total de questões. Questões já respondidas pelo aluno são excluídas.

    ### Parameters:
    >>> num_questoes (int): Total de questões desejadas no simulado.
    >>> materia_in_simulado (QuerySet): Materiais que fazem parte do simulado.
    >>> questoes_unicas (set): Conjunto de IDs de questões já selecionadas ou respondidas.
    >>> aluno (Aluno): Instância do aluno para o qual o simulado está sendo gerado.

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
        questoes_da_materia_objs = (
            Questao.objects.filter(conteudo__in=conteudos)
            .exclude(id__in=questoes_unicas)
            .order_by("?")[: questoes_por_materia[materia.nome]]
        )
        todos_questoes_objs.extend(questoes_da_materia_objs)

    questoes_unicas.update(questao.id for questao in todos_questoes_objs)

    return todos_questoes_objs


def filtra_questoes_simulado_natureza(
    num_questoes: int, materia_in_simulado, questoes_unicas: set, aluno: Aluno
) -> list:
    """
    Seleciona questões para o simulado com base em matérias de Ciências da Natureza.

    A função distribui as questões entre Biologia, Física e Química. Biologia recebe questões
    adicionais em caso de discrepâncias na distribuição. Questões já respondidas pelo aluno são excluídas.

    Parameters:
    ```bash
    num_questoes `(int)`: Total de questões desejadas no simulado.
    materia_in_simulado `(QuerySet)`: Materiais que fazem parte do simulado.
    questoes_unicas `(set)`: Conjunto de IDs de questões já selecionadas.
    aluno `(Aluno)`: Instância do aluno para o qual o simulado está sendo gerado.
    ```
    Returns:
    - list: Lista de questões selecionadas para o simulado.

    Example:
    >>> filtra_questoes_simulado_natureza(15, materias, set(), aluno_obj)
    >>> [<Questao: Questao1>, <Questao: Questao2>, ...]
    """
    questoes_por_materia = {
        "Biologia": num_questoes // 3,
        "Física": num_questoes // 3,
        "Química": num_questoes // 3,
    }

    total_questoes = sum(questoes_por_materia.values())
    discrepancia = num_questoes - total_questoes
    if discrepancia:
        questoes_por_materia["Biologia"] += discrepancia

    questoes_unicas.update(retorna_questoes_unicas(aluno))
    todos_questoes_objs = []
    for materia in materia_in_simulado:
        sub_materias_da_materia = SubMateria.objects.filter(materia=materia)
        conteudos = Conteudo.objects.filter(
            sub_materia__in=sub_materias_da_materia
        )  # Futura funcao para pegar conteudos que o usuario mais precisa AQUI.
        questoes_da_materia_objs = (
            Questao.objects.filter(conteudo__in=conteudos)
            .exclude(id__in=questoes_unicas)
            .order_by("?")[: questoes_por_materia[materia.nome]]
        )
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

    Parameters:\n
    ```bash
    num_questoes `(int)`: Total de questões desejadas a serem adicionadas de Matemática.\n
    materia_in_simulado `(QuerySet)`: Matéria(s) que faz(em) parte do simulado.\n
    questoes_unicas `(set)`: Conjunto de IDs de questões já selecionadas ou respondidas.\n
    aluno `(Aluno)`: Instância do aluno para o qual o simulado está sendo gerado.\n
    ```

    Returns:
    ```bash
    list: Lista questões para o simulado, incluindo as questões de Matemática selecionadas.
    ```

    Example:
    >>> questoes = []
    >>> filtra_questoes_simulado_matematica(questoes, 10, [<Materia: Matemática>], set(), aluno_obj)
    >>> [<Questao: Questao1>, <Questao: Questao2>, ... ,<Questao: Questao10>]
    """

    # Atualiza QUESTOES unicas
    questoes_unicas.update(retorna_questoes_unicas(aluno))

    print(define_proporcao_conteudos_provas(materia_in_simulado, num_questoes))
    # Recupera questoes excluindo questoes Unicas.
    questoes_ids = (
        Questao.objects.filter(conteudo__sub_materia__materia=materia_in_simulado[0])
        .exclude(id__in=questoes_unicas)
        .values_list("id", flat=True)
        .order_by("?")[:num_questoes]
    )
    todos_questoes_objs = list(Questao.objects.filter(id__in=questoes_ids))
    questoes_unicas.update(questao.id for questao in todos_questoes_objs)

    return todos_questoes_objs


def filtra_questoes_simulado_humanas(
    num_questoes: int, materia_in_simulado, questoes_unicas: set, aluno: Aluno
) -> list:
    """# `filtra_questoes_simulado_humanas`

    Esta função é projetada para filtrar e retornar questões para um simulado na área de Ciências Humanas.

    ## Parâmetros:

    - `num_questoes` (int): Número total de questões desejadas para o simulado.
    - `materia_in_simulado`: Materiais que serão incluídas no simulado.
    - `questoes_unicas` (set): Conjunto de questões únicas que já foram selecionadas.
    - `aluno`: Objeto representando o aluno para quem o simulado está sendo gerado.

    ## Retorno:

    - Retorna uma lista contendo objetos de questão que foram selecionados para o simulado.

    ## Descrição:

    A função começa definindo a proporção de questões para cada matéria dentro da área de Ciências Humanas. Em seguida, verifica se há alguma discrepância entre o número total de questões e a soma das questões de cada matéria, ajustando conforme necessário.

    A função então atualiza o conjunto de questões únicas e começa a buscar todas as questões relevantes para as matérias fornecidas, considerando sub-matérias e conteúdos associados.

    Finalmente, a função retorna todas as questões selecionadas.

    ```python
    >>>    filtra_questoes_simulado_humanas(num_questoes, materia_in_simulado, questoes_unicas, aluno)
    >>>  [<Questao: Questao1>, <Questao: Questao2>, ...]```
    """


def filtra_questoes_simulado_humanas(
    num_questoes: int, materia_in_simulado, questoes_unicas: set, aluno: Aluno
) -> list:
    ...

    questoes_por_materia = {
        "Filosofia": num_questoes * 0.20,
        "Sociologia": num_questoes * 0.20,
        "Geografia": num_questoes * 0.30,
        "História": num_questoes * 0.30,
    }
    total_questoes = sum(questoes_por_materia.values())
    discrepancia = num_questoes - total_questoes
    if discrepancia:
        questoes_por_materia["História"] += discrepancia

    questoes_unicas.update(retorna_questoes_unicas())

    todas_questoes_obj = []
    for materia in materia_in_simulado:
        sub_materias_da_materia = SubMateria.objects.filter(materia=materia)
        conteudos = Conteudo.objects.filter(sub_materia__in=sub_materias_da_materia)
        questoes_da_materia = Questao.objects.filter(conteudos__in=conteudos)
        todas_questoes_obj.extend(questoes_da_materia)

    questoes_unicas.update(questao.id for questao in todas_questoes_obj)

    return todas_questoes_obj


def retorna_questoes_com_proporcoes_niveis(lista_conteudo_questao:list, num_questoes:int):
    '''
    ## Retorna as questões com diferentes níveis de dificuldade.

    `lista_conteudo_questao`: Lista de conteúdos de questão disponíveis.\n
    `num_questoes`: Número total de questões desejadas.\n
    `max_tentativas`: Número máximo de tentativas para encontrar uma questão de um nível específico.\n
    ### Return: Lista de questões selecionadas.\n

    ```python
    >>> [questaoX, questaoY, questaoZ, ..., questaoN]
    ```
    '''
    questoes_selecionadas = []
    tentativas = 0

    while len(questoes_selecionadas) < num_questoes and tentativas:
        niveis = sample(range(1, 46), len(lista_conteudo_questao))
        for nivel in niveis:
            questao_encontrada = False
            tentativa_nivel = 0
            while not questao_encontrada and tentativa_nivel < len(lista_conteudo_questao):
                try:
                    conteudo = choice(lista_conteudo_questao)
                    questao = Questao.objects.filter(nivel=nivel, conteudo=conteudo).order_by("?").first()
                    if questao:
                        questoes_selecionadas.append(questao)
                        lista_conteudo_questao.remove(conteudo)
                        questao_encontrada = True

                except Questao.DoesNotExist:
                    tentativa_nivel += 1
                    continue

            if len(questoes_selecionadas) >= num_questoes:
                break
        tentativas += 1

    return questoes_selecionadas