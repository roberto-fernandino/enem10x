from pathlib import Path
import os
from django.utils.text import slugify
import docx
from docx2txt import process
import os
import re

BASE_DIR = Path(__file__).resolve().parent.parent
PATTERN_CONTEUDO = re.compile(r"(.+?) / ?(.+?)\n")


def replace_in_runs(paragraph, pattern, replacement):
    for run in paragraph.runs:
        if pattern.search(run.text):
            print(f"Encontrado em {run.text}")
            run.text = pattern.sub(replacement, run.text)


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
                    if conteudo_index != 1:
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


# print(alternativas('/home/roberto/projects/enem10x/src/leitores/questions3.docx'))
def extrair_enunciados(doc_obj):
    lista_enunciados = []
    texto_completo = "\n".join([paragrafo.text for paragrafo in doc_obj.paragraphs])

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


# print([enunciado for enunciado in lista_enunciados])


# print(extrair_enunciados('/home/roberto/projects/enem10x/src/leitores/questions3.docx'))


def define_image_path(instance, filename: str) -> str:
    """
    Define path para questoes que serao adcionadas.
    """
    ext = os.path.splitext(filename)[-1]
    filename = f"questao_{instance.questao.indentificador_unico}.{ext}"
    return Path(f"questoes/{filename}png")


def define_ranking_conteudo_prova(conteudos_errados: list, conteudos_acertados: list):
    """
    Gera um ranking de conteudos mais errados, acertados respectivamente de uma prova feita por um usario e os retorna no formato:\n
    \t - tuple(dict(ranking errados), dict(ranking acertados))"""

    ranking_piores = {}

    for conteudo in conteudos_errados:
        ranking_piores[conteudo.id] = ranking_piores.get(conteudo.id, 0) + 1

    ranking_piores = dict(
        sorted(ranking_piores.items(), key=lambda item: item[1], reverse=True)
    )

    ranking_melhores = {}

    for conteudo in conteudos_acertados:
        ranking_melhores[conteudo.id] = ranking_melhores.get(conteudo.id, 0) + 1

    ranking_melhores = dict(
        sorted(ranking_melhores.items(), key=lambda item: item[1], reverse=True)
    )
    return (
        ranking_piores,
        ranking_melhores,
    )


def procura_imagens() -> list:
    """
    Lista todas as imagens atualmente no diretorio de imagens e retorna uma lista contendo todas elas
    """
    imagens = os.listdir(f"{BASE_DIR}/media/imagens")
    return imagens


def docx_to_text(doc_obj):
    """
    Retorna o texto inteiro do .docx
    """
    full_text = []
    for paragraph in doc_obj.paragraphs:
        full_text.append(paragraph.text)
    return "\n".join(full_text)


def trata_conteudos(texto_extraido_do_docx: str) -> list:
    matches = PATTERN_CONTEUDO.findall(texto_extraido_do_docx)
    sub_subconteudo_global = []
    for match in matches:
        conteudo, sub_conteudo = match[0].strip(), match[1].strip()
        if len(conteudo) < 70 and len(sub_conteudo) < 70:
            sub_subconteudo_global.append([conteudo, sub_conteudo])
    return sub_subconteudo_global


def possui_img_tag(text: str) -> bool:
    return "[IMG]" in text


def checa_imagens_questoes(doc_obj):
    estamos_no_enunciado = False
    questoes = []
    questao = {
        "imagem_no_enunciado": False,
        "imagem_na_a": False,
        "imagem_na_b": False,
        "imagem_na_c": False,
        "imagem_na_d": False,
        "imagem_na_e": False,
    }
    for para in doc_obj.paragraphs:
        texto = para.text
        if "Questão-" in texto:
            if questao:
                questoes.append(questao)
            questao = {
            "imagem_no_enunciado": False,
            "imagem_na_a": False,
            "imagem_na_b": False,
            "imagem_na_c": False,
            "imagem_na_d": False,
            "imagem_na_e": False,
            }
            estamos_no_enunciado = True

        if re.match(r"[a-e]\$", texto):
            estamos_no_enunciado = False

        counter_img_enunciado = 0
        if estamos_no_enunciado:
            if possui_img_tag(texto):
                counter_img_enunciado += 1
                questao["imagem_no_enunciado"] = True

        if not estamos_no_enunciado:
            if "a$" in texto and possui_img_tag(texto):
                questao["imagem_na_a"] = True
            if "b$" in texto and possui_img_tag(texto):
                questao["imagem_na_b"] = True
            if "c$" in texto and possui_img_tag(texto):
                questao["imagem_na_c"] = True
            if "d$" in texto and possui_img_tag(texto):
                questao["imagem_na_d"] = True
            if "e$" in texto and possui_img_tag(texto):
                questao["imagem_na_e"] = True
    if questao:
        questoes.append(questao)
    questoes.pop(0)
    return questoes
doc_obj = docx.Document('app/leitores/questoesmat.docx')
questoes = checa_imagens_questoes(doc_obj)
for questao in questoes:
    print(questao)