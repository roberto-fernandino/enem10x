from pathlib import Path
import re
from itertools import islice
from usuarios.models import RankingConteudosErrados
import os

BASE_DIR = Path(__file__).resolve().parent.parent
PATTERN_CONTEUDO = re.compile(r"(.+?) / ?(.+?)\n")


def extrai_alternativas(text_after_docx_to_str_with_conteudos_aplicados):
    # Todo paragrafo existente no documento sendo adicionado a variavel
    texto_completo = text_after_docx_to_str_with_conteudos_aplicados
    # Dividindo todos paragrafos por questão, Assim salvando apenas a Questão, enunciado e alternativas
    questoes = texto_completo.split("Questão")[1:]
    # Lista de dicionarios, com alternativas de cada questão, um dicionario por questão
    alternativas_global = []
    for num, questao in enumerate(questoes, 1):  # Começar a enumerar de 1
        alternativas_questao = {}  # Dicionario com as alternativas para cada questão
        # Buscando as alternativas
        for index, letra in enumerate(
            ["a$", "b$", "c$", "d$", "e$", "w$"]
        ):  # Citando todas as alternativas possiveis , no caso 5
            inicio = questao.find(letra)
            # Se está na ultima letra (w$) definimos que é a ultima alternativa
            if index == 5:
                fim = len(questao)  # Definição do Fim
            else:
                # Procurando o início da próxima alternativa para definir o fim da alternativa atual
                proxima_letra = [
                    "a$",
                    "b$",
                    "c$",
                    "d$",
                    "e$",
                    "w$",
                ][index + 1]
                fim = questao.find(proxima_letra)
                if fim == -1:
                    fim = len(questao)
            if (
                inicio != -1 and fim != -1
            ):  # Certifica-se de que a variável inicio é diferente de -1 e Certifica-se de que a variável fim é diferente de -1.
                alternativa = questao[
                    inicio + 2 : fim
                ].strip()  # Atribui a proxima letra se não for a ultima
                if letra == "w$":
                    conteudo_index = alternativa.find("Conteudo:")
                    if conteudo_index != -1:
                        conteudo = alternativa[
                            conteudo_index + len("Conteudo:") :
                        ].strip()
                        alternativas_questao["conteudo"] = conteudo
                        alternativa = alternativa[:conteudo_index].strip()
                alternativas_questao[letra[0]] = alternativa
        # Adionando a lista o dicionario contido com as alternativas de cada questão
        chaves = {
            chave: valor
            for chave, valor in alternativas_questao.items()
            if chave in ["a", "b", "c", "d", "e", "w"]
        }
        alternativas_global.append(chaves)

    return alternativas_global  # Retorna alternativa_global


def extrair_enunciados(texto_completo_tratado: str) -> list:
    lista_enunciados = []
    texto_completo = texto_completo_tratado
    questoes = re.split("Questão-\d+", texto_completo)[1:]
    for questao in questoes:
        # Encontrar o início e o fim do enunciado da questão
        inicio_enunciado = questao.find("-") + 1
        fim_enunciado = min(
            [
                questao.find(letra)
                for letra in ["a$", "b$", "c$", "d$", "e$", "w$"]
                if questao.find(letra) != -1
            ]
        )  # Procurando as alternativas e quando achar volta um argumento
        # O minimo da lista é a primeira alternativa de resposta ou seja quando começa as alternativas, acaba o enunciado
        # Extrair o enunciado e adicionar à lista
        enunciado = questao[inicio_enunciado:fim_enunciado].strip()
        lista_enunciados.append(enunciado)

    return lista_enunciados


def lista_arquivos(diretorio) -> list:
    """
    Lista todas as imagens atualmente no diretorio de imagens e retorna uma lista contendo todas elas
    """
    arquivos = os.listdir(diretorio)
    return arquivos


def docx_to_text(doc_obj):
    """
    Retorna o texto inteiro do .docx
    """
    full_text = []
    for paragraph in doc_obj.paragraphs:
        full_text.append(paragraph.text)
    return "\n".join(full_text)


def extrai_conteudos(texto_extraido_do_docx: str) -> list:
    matches = PATTERN_CONTEUDO.findall(texto_extraido_do_docx)
    lista_conteudos_submaterias = []
    for match in matches:
        conteudo, sub_conteudo = (
            match[0].replace("Conteudo:", "").strip(),
            match[1].replace(";", "").strip(),
        )
        if len(conteudo) < 80 and len(sub_conteudo) < 80:
            lista_conteudos_submaterias.append([conteudo, sub_conteudo])
    return lista_conteudos_submaterias


def extrai_identificadores_unicos(texto_extraido_do_docx: str) -> list:
    return re.findall(r"Questão-\d+ \((\d+)\)", texto_extraido_do_docx)


def remove_todas_imagens_do_diretorio_local() -> None:
    imagens = lista_arquivos(f"{BASE_DIR}/media/questoes/")
    for imagem in imagens:
        if imagem != None:
            if os.path.exists(f"{BASE_DIR}/media/questoes/{imagem}"):
                os.remove(f"{BASE_DIR}/media/questoes/{imagem}")


def retorna_ranking_de_conteudos_geral(provas: list) -> dict:
    """
    Retorna os top 5 conteúdos com a maior diferença entre erros e acertos para um conjunto de provas.

    Dada uma lista de objetos de prova, esta função calcula o ranking dos conteúdos com base na
    diferença entre o número de erros e acertos para cada conteúdo. O resultado é um dicionário
    contendo os 5 conteúdos com a maior diferença, ordenados em ordem decrescente.

    Parâmetros:
    -----------
    provas : list
        Uma lista contendo objetos de prova. Cada objeto de prova deve ter os atributos
        `ranking_piores_conteudos` e `ranking_melhores_conteudos`, que são dicionários mapeando
        conteúdos para o número de erros e acertos, respectivamente.

    Retorna:
    --------
        Um dicionário contendo os top 5 conteúdos com a maior diferença entre erros e acertos.
        As chaves são os nomes dos conteúdos e os valores são a diferença calculada.

    Exemplo:
    --------
    >>> provas = [Prova(ranking_piores_conteudos={'Geometria plana': 5, 'Geometria Analitica': 2},
                        ranking_melhores_conteudos={'Geometria plana': 2, 'Geometria Analitica': 1})]
    >>> retorna_ranking_de_conteudos_geral(provas)
    {'Geometria plana': 3, 'Geometria Analitica': 1}
    """
    conteudos_geral_dict = {}

    for prova in provas:
        piores_conteudos_ranking_prova = prova.ranking_piores_conteudos or {}
        melhores_conteudos_ranking_prova = prova.ranking_melhores_conteudos or {}

        if piores_conteudos_ranking_prova:
            for conteudo, erros in piores_conteudos_ranking_prova.items():
                conteudos_geral_dict[conteudo] = (
                    conteudos_geral_dict.get(conteudo, 0) + erros
                )

        if melhores_conteudos_ranking_prova:
            for conteudo, acertos in melhores_conteudos_ranking_prova.items():
                conteudos_geral_dict[conteudo] = (
                    conteudos_geral_dict.get(conteudo, 0) - acertos
                )

    top_5_conteudos_errados = dict(
        islice(
            sorted(
                conteudos_geral_dict.items(), key=lambda item: item[1], reverse=True
            ),
            5,
        )
    )

    return top_5_conteudos_errados


def organiza_provas_por_tipo(sender, aluno) -> dict:
    """
    ### Função pra retornar dentre as ultimas 15 provas realizadas do usuario os ultimos simulados ali dentro.
    --------
    ### Objetivo:
        - Recuperar os conteudos mais errados dos simulados do usuarios nos últimos tempos.
        - Usar esses dados então pra criação de provas pro usuario estudar e focar nos conteúdos que ele mais precisa.
    --------
    ## Retorna:

    ```python
    {
        "Matemática": 'num_provas',
        "Ciencias Humanas": 'num_provas',
        "Ciencias Natureza": 'num_provas',
        "Linguagens": 'num_provas',

    }
    ```

    """
    simulados_tipo = {}
    provas_do_usuario = sender.objects.filter(aluno=aluno).order_by("-data_feita")[:15]
    for prova in provas_do_usuario:
        tipo_simulado = prova.simulado if prova.simulado else None
        if tipo_simulado:
            if tipo_simulado not in simulados_tipo:
                simulados_tipo[tipo_simulado] = []
            simulados_tipo[tipo_simulado].append(prova)
    return simulados_tipo


def atualiza_ranking_por_tipo(aluno, tipo, provas_list: list):
    """
    ### Atualiza o ranking do usuario de acordo com seu top 5 conteudos errados calculados por `retorna_ranking_de_conteudos_geral`
    --------

    --------
    ## Retorna:

        ```python
        None
        ```
    --------

    # Exemplo:
    --------
    ## Ranking_antigo = {
        1:Conteudo_X,
        2:Conteudo_Y,
        3:Conteudo_Z,
        4:Conteudo_W,
        5:Conteudo_A,
    }\n

    ## Rankgin_novo = {
        1:Conteudo_Y,
        2:Conteudo_X,
        3:Conteudo_Z,
        4:Conteudo_A,
        5:Conteudo_G,
    }
    --------




    """
    from materiais.models import Conteudo

    ranking_do_tipo = retorna_ranking_de_conteudos_geral(provas_list)
    ranking_conteudos_errados, _ = RankingConteudosErrados.objects.get_or_create(
        aluno=aluno, tipo_simulado=tipo
    )
    counter = 1
    for conteudo in Conteudo.objects.filter(pk__in=ranking_do_tipo.keys()):
        campo = f"conteudo_{counter}"
        setattr(ranking_conteudos_errados, campo, conteudo)
        counter += 1

    ranking_conteudos_errados.save()
