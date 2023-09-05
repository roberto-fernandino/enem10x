from pathlib import Path
import os
from django.utils.text import slugify
import docx
from docx2txt import process
import os
import re

BASE_DIR = Path(__file__).resolve().parent.parent
PATTERN_SUP_TAG = re.compile(r"(\d+(\.\d+)?x10\s*)(\-?\d+)")
PATTERN_CONTEUDO = re.compile(r"(.+?) / ?(.+?)\n")


'''def get_conteudos(texto_extraido_do_docx_com_conteudos_aplicados: str) -> list:
    conteudo_global = []
    sub_subconteudo_global = []
    texto_completo = texto_extraido_do_docx_com_conteudos_aplicados

    # Dividir texto pelo marcador "Conteudo"
    conteudos = texto_completo.split("Conteudo:")[1:]  # ignora o primeiro fragmento
    for num, conteudo in enumerate(conteudos, 1):
        # Dicionário para armazenar o conteudo de cada questão
        conteudo_questao = {}

        # O fim do conteudo informado como  ;
        fim = conteudo.find(";")

        # Armazenazenando o Conteudo das questões
        conteudo_questao["conteudo"] = conteudo[:fim].strip()

        # Adiciona este dicionário ao conteúdo global
        conteudo_global.append(conteudo_questao)

    for index, conteudo in enumerate(conteudo_global):
        sub_conteudo = conteudo["conteudo"].split("/")
        sub_subconteudo_global.append(sub_conteudo)

    return sub_subconteudo_global
'''


# print(get_conteudos('app/leitores/questionsfinal.docx'))


def alternativas(text_after_docx_to_str_with_conteudos_aplicados):
    # Todo paragrafo existente no documento sendo adicionado a variavel
    texto_completo  = text_after_docx_to_str_with_conteudos_aplicados
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
def extrair_enunciados(arquivo):
    lista_enunciados = []

    doc = docx.Document(arquivo)
    texto_completo = "\n".join([paragrafo.text for paragrafo in doc.paragraphs])

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
    ext = os.path.splitext(filename)[1]
    filename = f'enem.{ext.lstrip(".")}'
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
    '''
    Lista todas as imagens atualmente no diretorio de imagens e retorna uma lista contendo todas elas'''
    imagens = os.listdir(f"{BASE_DIR}/media/imagens")
    return imagens


def apply_sup_tags(doc_obj, doc_path):
    """
    Aplica suptags em notacoes cientificas, e salva no arquivo.docx.
    """
    for paragraph in doc_obj.paragraphs:
        new_text = paragraph.text
        for match in re.finditer(PATTERN_SUP_TAG, paragraph.text):
            whole, base, expoente = match.group(0), match.group(1), match.group(3)
            if "<sup>" not in whole:
                new_text = new_text.replace(whole, f"{base}<sup>{expoente}</sup>")
        for run in paragraph.runs:
            run.clear()

        paragraph.add_run(new_text)
    doc_obj.save(doc_path)


def docx_to_text(doc_obj):
    """
    Retorna o texto inteiro do .docx
    """
    full_text = []
    for paragraph in doc_obj.paragraphs:
        full_text.append(paragraph.text)
    return "\n".join(full_text)


def apply_conteudos(texto_extraido_do_docx_em_string: str) -> str:
    """
    Aplica conteudos no texto e retorna uma lista com os conteudos de cada questao em ordem.
    """
    texto_modificado = texto_extraido_do_docx_em_string
    matches = list(PATTERN_CONTEUDO.finditer(texto_extraido_do_docx_em_string))
    for match in matches:
       
        whole, conteudo, sub_conteudo = match.group(0), match.group(1), match.group(2)
        if len(conteudo) < 50 and len(sub_conteudo) < 50:  
            replace = f"Conteudo: {conteudo} / {sub_conteudo};\n"
            texto_modificado = texto_modificado.replace(whole, replace, 1)
    return texto_modificado


def get_conteudos(texto_extraido_do_docx: str) -> list:
    matches = PATTERN_CONTEUDO.findall(texto_extraido_do_docx)
    print(matches)
    sub_subconteudo_global = []
    for match in matches:
        conteudo, sub_conteudo = match[0].strip(), match[1].strip()
        if len(conteudo) < 70  and len(sub_conteudo) < 70:
            sub_subconteudo_global.append([conteudo, sub_conteudo])
    return sub_subconteudo_global

doc_obj = docx.Document("app/leitores/P002284[1].docx")
apply_sup_tags(doc_obj=doc_obj, doc_path="app/leitores/P002284[1].docx")
doc_text_completo = docx_to_text(doc_obj)
conteudos = get_conteudos(doc_text_completo)
doc_text_conteudos_aplicados = apply_conteudos(doc_text_completo)
alternativa_s = alternativas(doc_text_conteudos_aplicados)
print(alternativa_s, conteudos)

