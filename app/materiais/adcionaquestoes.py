from materiais.models import Questao, Materia, Nivel, Tipo, SubMateria, Conteudo
from materiais.funcs import (
    procura_imagens,
    process,
    extrair_enunciados,
    extrai_alternativas,
    BASE_DIR,
    apply_sup_tags,
    trata_conteudos,
    docx_to_text,
    trata_conteudos,
)
from subprocess import run
from docx import Document


def adciona_questoes(arquivo_path: str, materia: str):
    """Adciona questoes no banco de dados."""

    # Cria doc_obj e variaveis que serao utilizadas no script inteiro
    DOC_OBJ = Document(arquivo_path)
    apply_sup_tags(doc_obj=DOC_OBJ, doc_path=arquivo_path)
    DOC_ALL_TEXT = docx_to_text(DOC_OBJ)
    DOC_ALL_TEXT_CONTEUDOS_APPLIED = trata_conteudos(DOC_ALL_TEXT)
    CONTEUDOS_LIST_LIST = trata_conteudos(DOC_ALL_TEXT)
    ALTERNATIVAS_LIST_DICT = extrai_alternativas(DOC_ALL_TEXT_CONTEUDOS_APPLIED)

    # Seta diretorio para salvar imagens
    img_dir = BASE_DIR / "media/imagens/"

    # Processa o arquivo e salva as imagens no direitorio especificado em img_dir
    process(arquivo_path, img_dir)

    # Inicia contagem que sera utilizada para contar imagens guardadas, nomealas em ordem.
    count = 1

    # Salva quantidade de imagens total no diretorio para controle.
    img_count = len(procura_imagens())

    # Checa se existem imagens se existir seta tem_imagens pra True
    tem_imagens = False
    if img_count > 1:
        tem_imagens = True

    # Inicia contagens para questoes.
    questoes_count = 0

    for questao in extrair_enunciados(DOC_OBJ):
        # Objeto questao
        questao_obj = Questao()
        questao_obj.enunciado = questao
        
        # Salva em um dicionario as alternativas e conteudos atuais
        actual_alternativas_dict = ALTERNATIVAS_LIST_DICT[questoes_count]
        actual_conteudos_list = CONTEUDOS_LIST_LIST[questoes_count]

        # Lista de opcoes
        opcoes_list = []
        
        # Salva todas as opcoes de a-e na lista de opcoes
        opcoes_list = [actual_alternativas_dict[letra] for letra in "abcde"]
        
        # Salva no objeto a opcao correta
        questao_obj.opcao_correta = actual_alternativas_dict["w"]
        
        # Salva no objeto todas opcoes
        questao_obj.opcoes = opcoes_list

        # Materia obj = materia_
        materia_, _ = Materia.objects.get_or_create(nome=materia)
        # Submateria obj = sub_materia

        sub_materia, _ = SubMateria.objects.get_or_create(
            nome=actual_conteudos_list[1], materia=materia_
        )
        conteudo, _ = Conteudo.objects.get_or_create(
            nome=actual_conteudos_list[0], sub_materia=sub_materia
        )

        if tem_imagens:
            img_path = img_dir / f"image{count}.png"
            with img_path.open("rb") as image_file:
                questao_obj.imagem.save("questao", image_file, save=False)
                print(f"{count} Imagens adcionadas!")
                count += 1

            if (img_count + 1) == count:
                tem_imagens = False

        questao_obj.save()
        questao_obj.conteudo.add(conteudo)
        questoes_count += 1

        print(f"{questoes_count} Questoes adcionadas com sucesso!")
