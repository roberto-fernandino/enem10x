from materiais.models import Questao, Materia, SubMateria, Conteudo, OpcaoImagem
from materiais.funcs import (
    process,
    extrair_enunciados,
    extrai_alternativas,
    BASE_DIR,
    docx_to_text,
    extrai_conteudos,
    extrai_identificadores_unicos,
    remove_todas_imagens_do_diretorio_local,
    lista_arquivos,
)
from subprocess import run
from docx import Document
from materiais.tratamentos import tratamento_geral_pra_extracao
import os

def adciona_questoes(arquivo_path: str, materia: str):
    """Adciona questoes no banco de dados."""

    # Cria doc_obj e variaveis que serao utilizadas no script inteiro
    DOC_OBJ = Document(arquivo_path)
    tratamento = tratamento_geral_pra_extracao(doc_obj=DOC_OBJ, doc_path=arquivo_path)
    tratamento.Tratamento()
    img_check_questoes_list_dict = tratamento.checa_imagens_questoes()
    DOC_ALL_TEXT = docx_to_text(DOC_OBJ)
    DOC_ALL_TEXT = tratamento.Tratamento_sup_tags(DOC_ALL_TEXT)
    DOC_ALL_TEXT = tratamento.trata_conteudos(
        texto_extraido_do_docx_em_string=DOC_ALL_TEXT
    )
    identificadores_unicos_list = extrai_identificadores_unicos(DOC_ALL_TEXT)
    ALTERNATIVAS_LIST_DICT = extrai_alternativas(DOC_ALL_TEXT)
    CONTEUDOS_LIST_LIST = extrai_conteudos(DOC_ALL_TEXT)

    
    
    # Seta diretorio para salvar imagens
    img_dir = BASE_DIR / "media/questoes/"

    # Processa o arquivo e salva as imagens no direitorio especificado em img_dir
    process(arquivo_path, img_dir)

    # Inicia contagem que sera utilizada para contar imagens guardadas, nomealas em ordem.
    count = 1

    imagem_fields_map = {
        "a": "imagem_a",
        "b": "imagem_b",
        "c": "imagem_c",
        "d": "imagem_d",
        "e": "imagem_e",
    }
    # Salva quantidade de imagens total no diretorio para controle.
    img_count = len(lista_arquivos(img_dir))

    # Checa se existem imagens se existir seta tem_imagens pra True
    tem_imagens = False
    if img_count > 1:
        tem_imagens = True

    # Inicia contagens para questoes.
    questoes_count = 0

    for questao in extrair_enunciados(DOC_ALL_TEXT):
        # Objeto questao
        img_path = img_dir / f"image{count}.png"

        questao_obj = Questao()
        questao_obj.enunciado = questao
        questao_obj.identificador_unico = identificadores_unicos_list[questoes_count]
        # Salva no objeto a opcao correta
        actual_alternativas_dict = ALTERNATIVAS_LIST_DICT[questoes_count]
        questao_obj.opcao_correta = actual_alternativas_dict["w"]
        actual_images_check_dict = img_check_questoes_list_dict[questoes_count]
        print(actual_images_check_dict)
        if tem_imagens:
            if actual_images_check_dict["imagem_no_enunciado"]:
                print('Tem imagem no enunciado')
                with img_path.open("rb") as image_file:
                    ext = os.path.splitext(img_path)[-1]
                    questao_obj.imagem_enunciado.save(f"questao_enunciado_{questao_obj.identificador_unico}.{ext}",image_file, save=False)
                    print('Imagem do enunciado adcionada')
                count += 1
                img_path = img_dir / f"image{count}.png"

        questao_obj.save()
        questao_imgs_obj = OpcaoImagem.objects.create(questao=questao_obj)
        questao_imgs_obj.questao = questao_obj
        # Salva em um dicionario as alternativas e conteudos atuais
        actual_conteudos_list = CONTEUDOS_LIST_LIST[questoes_count]

        # Lista de opcoes
        opcoes_list = []
        # Salva todas as opcoes de a-e na lista de opcoes
        opcoes_list = [actual_alternativas_dict[letra] for letra in "abcde"]
        for chave, opcao in enumerate('abcde'):
            if actual_images_check_dict[f"imagem_na_{opcao}"] == True:
                with img_path.open("rb") as image_file:
                    ext = os.path.splitext(img_path)[-1]
                    field_name = imagem_fields_map[opcao]
                    getattr(questao_imgs_obj, field_name).save(f"questoes_{questao_obj.identificador_unico}_{opcao}.{ext}", image_file, save=False)
                count += 1
                img_path = img_dir / f"image{count}.png"
        print(opcoes_list)

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

        if (img_count + 1) == count:
            tem_imagens = False

        questao_obj.conteudo.add(conteudo)
        questao_imgs_obj.save()
        questoes_count += 1
        questao_obj.save()

        print(f"{questoes_count} Questoes adcionadas com sucesso!")
        
    # Limpa img_dir
    remove_todas_imagens_do_diretorio_local()