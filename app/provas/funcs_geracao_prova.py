from .funcs import (
filtra_questoes_simulado_humanas,
filtra_questoes_simulado_linguagens,
filtra_questoes_simulado_matematica,
filtra_questoes_simulado_natureza
)
from usuarios.models import Aluno
from materiais.models import SubMateria, Conteudo, Questao, Materia, Simulado

def geracao_simulado(simulado_id_list:list, num_questoes:int, aluno:Aluno):
    simulados = Simulado.objects.filter(pk__in=simulado_id_list).prefetch_related('materia')
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
            questoes.extend(filtra_questoes_simulado_matematica(
                num_questoes,
                materia_in_simulado,
                questoes_unicas,
                aluno,
            ))
        # Se um dos simulados for de ciencias da natureza

        elif len(materia_in_simulado) == 3:
            questoes.extend(filtra_questoes_simulado_natureza(
                num_questoes,
                materia_in_simulado,
                questoes_unicas,
                aluno,
            ))
        # Se um dos simulados for de Linguagens

        elif len(materia_in_simulado) == 5:
            questoes.extend(filtra_questoes_simulado_linguagens(
                num_questoes,
                materia_in_simulado,
                questoes_unicas,
                aluno,
            ))
    return questoes, simulados    


def geracao_automatica_lista(materia_id_list:list, num_questoes:int):
    """
    ### Parâmetros

    1. `materia_id_list` (`list`): Uma lista de identificadores (IDs) representando as matérias.
    2. `num_questoes` (`int`): Número de questões a serem selecionadas por matéria.

    ### Descrição

    Esta função tem como objetivo gerar uma lista de questões de forma automática, baseada em matérias específicas. A função faz isso buscando as questões relacionadas a cada matéria fornecida e selecionando um número definido de questões para cada uma delas.

    ### Processo

    1. **Seleção das Matérias**: A função começa filtrando os objetos `Materia` com base nos IDs fornecidos na `materia_id_list`.
    2. **Busca de Submatérias e Conteúdos**: Para cada matéria, a função busca as submatérias relacionadas (`SubMateria`) e, em seguida, os conteúdos (`Conteudo`) ligados a estas submatérias.
    3. **Seleção de Questões**:
    - A função busca as questões (`Questao`) relacionadas a estes conteúdos.
    - As questões são selecionadas aleatoriamente (ordenadas por `?`).
    - A função garante que cada questão é única (usando um conjunto `questoes_unicas`) e limita o número de questões selecionadas por matéria ao valor de `num_questoes`.

    ### Retorno

    - **Tupla**: A função retorna uma tupla contendo duas listas:
    1. `questoes` (`list`): Lista de objetos `Questao` selecionados.
    2. `materias` (`list`): Lista de objetos `Materia` correspondentes aos IDs fornecidos.

    ### Exemplo de Uso

    ```python
    lista_materias = [1, 2, 3]  # IDs das matérias
    num_questoes_por_materia = 5

    questoes_selecionadas, materias_selecionadas = geracao_automatica_lista(lista_materias, num_questoes_por_materia)

    # Agora, questoes_selecionadas contém as questões selecionadas e materias_selecionadas as matérias correspondentes.
    ```

    ### Notas

    - A função assume que os modelos `Materia`, `SubMateria`, `Conteudo` e `Questao` estão devidamente definidos e relacionados no sistema.
    - A função pode retornar menos questões do que o solicitado se o número total de questões únicas disponíveis for menor que `num_questoes`.
    - A ordem aleatória das questões (`order_by("?")`) pode impactar o desempenho, especialmente com um grande número de questões. Considere alternativas se o desempenho for uma preocupação.
"""
    materias = Materia.objects.filter(pk__in=materia_id_list)
    questoes_unicas = set()
    questoes = []

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
    return questoes, materias