from materiais.models import Questao, Materia, Nivel, Tipo, SubMateria, Conteudo
from materiais.funcs import (
    procura_imagens,
    process,
    extrair_enunciados,
    alternativas,
    BASE_DIR,
    apply_sup_tags,
    apply_conteudos,
    docx_to_text,
    get_conteudos,
)
from subprocess import run
from docx import Document


def adciona_questoes(arquivo: str, materia: str):
    """Adciona questoes no banco de dadosFormato:
    conteudo,
    enunciado,
    imagem,
    opcao correta"""

    # Cria doc_obj e variaveis que serao utilizadas no script inteiro
    DOC_OBJ = Document(arquivo)
    apply_sup_tags(doc_obj=DOC_OBJ, doc_path=arquivo)
    DOC_ALL_TEXT = docx_to_text(DOC_OBJ)
    DOC_ALL_TEXT_CONTEUDOS_APPLIED = apply_conteudos(DOC_ALL_TEXT)
    ALTERNATIVAS_LIST_DICT = alternativas(DOC_ALL_TEXT_CONTEUDOS_APPLIED)
    CONTEUDOS_LIST_LIST = get_conteudos(DOC_ALL_TEXT)
    
    # Seta diretorio para salvar imagens
    img_dir = BASE_DIR / "media/imagens/"

    # Processa o arquivo e salva as imagens no direitorio especificado em img_dir
    process(arquivo, img_dir)

    # Inicia contagem que sera utilizada para contar imagens guardadas, nomealas em ordem.
    count = 1

    # Salva quantidade de imagens total no diretorio para controle.
    img_count = len(procura_imagens())
    tem_imagens = False

    # Checa se existem imagens se existir seta tem_imagens pra True
    if img_count > 1:
        tem_imagens = True

    # Inicia contagens para questoes.
    questoes_count = 0

    # Salva todas as alternativas
    OPCOES_DICT_LIIST = alternativas(arquivo)

    for questao in extrair_enunciados(arquivo):
        questao_obj = Questao()
        questao_obj.enunciado = questao
        opcoes_list = []
        actual_dict = OPCOES_DICT_LIIST[questoes_count]
        opcoes_list = [actual_dict[letra] for letra in "abcde"]
        questao_obj.opcao_correta = actual_dict["w"]
        questao_obj.opcoes = opcoes_list
        materia, _ = Materia.objects.get_or_create(nome=actual_dict["m"])
        sub_materia, _ = SubMateria.objects.get_or_create(
            nome=actual_dict["s"], materia=materia
        )
        conteudo, _ = Conteudo.objects.get_or_create(
            nome=actual_dict["t"], sub_materia=sub_materia
        )
        nivel, _ = Nivel.objects.get_or_create(nivel=actual_dict["n"])
        questao_obj.conteudo = conteudo
        questao_obj.nivel = nivel
        questao_obj.tipo = actual_dict["p"]

        if tem_imagens:
            img_path = img_dir / f"image{count}.png"
            with img_path.open("rb") as image_file:
                questao_obj.imagem.save("questao", image_file, save=False)
                print(f"{count} Imagens adcionadas!")
                count += 1

            if (img_count + 1) == count:
                tem_imagens = False

        questao_obj.save()
        questoes_count += 1

        print(f"{questoes_count} Questoes adcionadas com sucesso!")
