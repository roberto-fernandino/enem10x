from math import floor
from materiais.models import (
    Conteudo,
    Questao,
    SubMateria,
    QuestaoRespondida,
    GrupoConteudo,
    Materia,
)
from usuarios.models import Aluno
from random import sample, randint, choice, shuffle


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


def define_proporcao_conteudos_provas(materia_in_simulado: list, num_questoes: int):
    """

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
    ### Onde:
    {`id_conteudo`:num_questoes_por_conteudo}
    """
    pass


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
    num_questoes: int, questoes_unicas: set, aluno: Aluno
) -> list:
    """
    ## Filtra e adiciona questões de Matemática ao conjunto de questões fornecido.

    Esta função seleciona questões de matemática para um simulado, baseando-se nas questões
    ainda não respondidas pelo aluno. As questões selecionadas são então adicionadas ao conjunto
    de questões fornecido (argumento `questoes`) e também são atualizadas no conjunto de questões únicas.

    ## Parameters:\n
    ```bash
    num_questoes `(int)`: Total de questões desejadas a serem adicionadas de Matemática.\n
    materia_in_simulado `(QuerySet)`: Matéria(s) que faz(em) parte do simulado.\n
    questoes_unicas `(set)`: Conjunto de IDs de questões já selecionadas ou respondidas.\n
    aluno `(Aluno)`: Instância do aluno para o qual o simulado está sendo gerado.\n
    ```

    ## Returns:
    ```bash
    list: Lista questões para o simulado, incluindo as questões de Matemática selecionadas.
    ```

    ## Example:
    >>> questoes = []
    >>> filtra_questoes_simulado_matematica(questoes, 10, [<Materia: Matemática>], set(), aluno_obj)
    >>> [<Questao: Questao1>, <Questao: Questao2>, ... ,<Questao: Questao10>]
    """

    # Atualiza QUESTOES unicas
    questoes_unicas.update(retorna_questoes_unicas(aluno))
    materia = Materia.objects.get(id=1)
    conteudos_de_mat = Conteudo.objects.filter(sub_materia__materia=materia)
    questoes_list = Questao.objects.filter(conteudo__in=conteudos_de_mat).order_by("?")[
        :num_questoes
    ]

    """# Recupera questoes excluindo questoes Unicas.
    questoes_ids = (
        Questao.objects.filter(conteudo__sub_materia__materia=materia_in_simulado[0])
        .exclude(id__in=questoes_unicas)
        .values_list("id", flat=True)
        .order_by("?")[:num_questoes]
    )
    todos_questoes_objs = list(Questao.objects.filter(id__in=questoes_ids))
    """

    questoes_unicas.update(questao.id for questao in questoes_list)

    return questoes_list


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

    questoes_unicas.update(retorna_questoes_unicas(aluno))

    todas_questoes_obj = []
    for materia in materia_in_simulado:
        sub_materias_da_materia = SubMateria.objects.filter(materia=materia)
        conteudos = Conteudo.objects.filter(sub_materia__in=sub_materias_da_materia)
        questoes_da_materia = Questao.objects.filter(conteudos__in=conteudos)
        todas_questoes_obj.extend(questoes_da_materia)

    questoes_unicas.update(questao.id for questao in todas_questoes_obj)

    return todas_questoes_obj


def retorna_questoes_com_proporcoes_niveis(
    lista_conteudo_questao: dict, num_questoes: int
) -> list:
    """
    ## Retorna as questões com diferentes níveis de dificuldade.

    `lista_conteudo_questao`: Lista de conteúdos de questão disponíveis.\n
    `num_questoes`: Número total de questões desejadas.\n
    ### Return: Lista de questões selecionadas.\n

    ```python
    >>> [questaoX, questaoY, questaoZ, ..., questaoN]
    ```

    ### Como Funciona:
    1. Inicializa uma lista vazia para armazenar as questões selecionadas.
    2. Gera uma lista de todos os níveis possíveis e a embaralha.
    3. Itera sobre cada conteúdo da `lista_conteudo_questao`.
    4. Tenta encontrar uma questão que corresponda ao conteúdo e nível.
    5. Se encontrada, adiciona à lista de questões selecionadas.
    6. Se não, tenta encontrar uma questão com o mesmo conteúdo e um nível adjacente.
    7. Se ainda não encontrada, tenta encontrar uma questão em um conteúdo diferente do mesmo grupo.
    8. Retorna a lista de questões selecionadas quando o número desejado de questões é alcançado.
    """
    questoes_selecionadas = []
    todos_niveis = list(range(1, 46))
    shuffle(todos_niveis)
    print(f"todos_niveis: {todos_niveis}")
    niveis_utilizados = []
    print(f"lista_conteudo_questao: {lista_conteudo_questao}")
    for conteudo in lista_conteudo_questao:
        print(f"questoes_selecionadas: {questoes_selecionadas}")
        nivel = choice(todos_niveis)
        questao = (
            Questao.objects.filter(nivel=nivel, conteudo=conteudo)
            .exclude(id__in=[q.id for q in questoes_selecionadas])
            .first()
        )  # Tenta uma questao com os parametros inciais.

        if questao:  # Se achar
            questoes_selecionadas.append(questao)  # Adicina na lista.
            todos_niveis.remove(nivel)  # Remove nivel da lista de niveis disponives.
            niveis_utilizados.append(nivel)
            continue  # Pula pro proximo conteudo

        questao = tenta_achar_questao_com_mesmo_conteudo_com_niveis_diferentes(
            conteudo, nivel, niveis_utilizados, questoes_selecionadas
        )

        if questao is not None:
            questoes_selecionadas.append(questao)
            continue

        if len(questoes_selecionadas) >= num_questoes:
            return questoes_selecionadas

        # Se nao achar com outro niveis nesse conteudo pega de outro conteudo do mesmo grupo.
        if (
            questao is None and len(questoes_selecionadas) < num_questoes
        ):  # Se nao achar nenhuma questão ainda
            grupo_conteudo = GrupoConteudo.objects.filter(
                conteudos__id=conteudo
            ).first()  # Pega o grupo do conteudo
            for (
                conteudo_do_grupo
            ) in grupo_conteudo.conteudos.all():  # Itera por todos conteudos do grupo
                questao = Questao.objects.filter(
                    conteudo=conteudo_do_grupo, nivel=nivel
                ).first()  # Tenta achar uma questao com o nivel e com o conteudo (do mesmo grupo)

                if questao:  # Se achar
                    questoes_selecionadas.append(questao)  # Adiciona na lista.
                    todos_niveis.remove(
                        nivel
                    )  # Remove nivel da lista de niveis disponives.

                    if (
                        len(questoes_selecionadas) >= num_questoes
                    ):  # Confere se já pegou todas as questões.
                        return questoes_selecionadas  # Caso sim retorna.
                    break  # Sai do for de conteudos proximos e volta ao for dos conteudos originais.

                questao = tenta_achar_questao_com_mesmo_conteudo_com_niveis_diferentes(
                    conteudo_do_grupo, nivel, niveis_utilizados, questoes_selecionadas
                )
                # Se achou questao com outro nivel
                if questao is not None:
                    questoes_selecionadas.append(questao)
                    break

                if (
                    len(questoes_selecionadas) >= num_questoes
                ):  # Confere mais uma vez se ja escolheu todas questões.
                    return questoes_selecionadas

    return questoes_selecionadas


def tenta_achar_questao_com_mesmo_conteudo_com_niveis_diferentes(
    conteudo, nivel, niveis_utilizados: list, questoes_selecionadas: list
) -> None | Questao:
    """
    ## Tenta encontrar questões com o mesmo conteúdo e níveis adjacentes.

    `conteudo`: O conteúdo da questão desejada.\n
    `nivel`: O nível da questão desejada.\n
    `niveis_utilizados`: Lista de níveis já utilizados.\n
    ### Return: A questão encontrada ou None.\n

    ```python
    >>> questao or None
    ```

    ### Como Funciona:
    1. Gera uma lista de números de -3 a 3 e a embaralha.
    2. Itera sobre cada número da lista.
    3. Calcula um nível adjacente somando o número ao `nivel`.
    4. Verifica se o `nivel_adjacente` não está na lista `niveis_utilizados`.
    5. Se não está, tenta encontrar uma questão que corresponda ao `conteudo` e `nivel_adjacente`.
    6. Se encontrada, retorna a questão.
    7. Se não encontrada após iterar sobre todos os números, retorna None.
    """
    range_list = list(range(-3, 4))
    shuffle(range_list)

    for i in range_list:
        nivel_adjacente = min(
            max(1, nivel + i), 45
        )  # Tenta achar com o mesmo conteudo porem 6 niveis de discrepancia.

        if nivel_adjacente not in niveis_utilizados:
            questao = (
                Questao.objects.filter(nivel=nivel, conteudo=conteudo)
                .exclude(id__in=[q.id for q in questoes_selecionadas])
                .first()
            )  # Tenta uma questao com os parametros inciais.

            if questao:
                return questao
    return


def cria_lista_de_conteudos_apos_proporcao_definida(conteudo_questoes_dict: dict):
    lista_conteudo_questao = []

    for conteudo, qtd_questoes in conteudo_questoes_dict.items():
        for i in range(0, qtd_questoes):
            lista_conteudo_questao.append(conteudo)

    return lista_conteudo_questao
