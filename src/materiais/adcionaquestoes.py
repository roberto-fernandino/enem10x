from materiais.models import Questao
from materiais.funcs import procura_imagens, process, extrair_enunciados, alternativas, BASE_DIR
from subprocess import run

def adciona_questoes(arquivo:str):
    """Adciona questoes no banco de dadosFormato:
    enunciado,
    imagem,
    opcao correta"""
    img_dir = BASE_DIR / 'media/imagens/'
    imagens = process(arquivo, img_dir)
    count = 1
    img_count = len(procura_imagens())
    tem_imagens = False
    questoes_count = 0
    opcoes_dict_list = alternativas(arquivo)
    if img_count > 1:
        tem_imagens = True   
    for questao in extrair_enunciados(arquivo):
        questao_obj = Questao()
        questao_obj.enunciado = questao
        opcoes_list = []
        actual_dict = opcoes_dict_list[questoes_count]
       
        opcoes_list = [actual_dict[letra] for letra in 'abcde']
        questao_obj.opcao_correta = actual_dict['r']       
        questao_obj.opcoes = opcoes_list
        if tem_imagens:
            img_path = img_dir / f'image{count}.png'
            with img_path.open('rb') as image_file:
                questao_obj.imagem.save('questao', image_file, save=False)
                print(f'{count} Imagens adcionadas!')
                count += 1

            if (img_count + 1) == count:
                tem_imagens = False

        questao_obj.save()
        questoes_count += 1
        
        print(f'{questoes_count} Questoes adcionadas com sucesso!')

        
