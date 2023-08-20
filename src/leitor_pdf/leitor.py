from PyPDF2 import PdfReader

def Recupera_questoes_enem(path_to_pdf: str, ):
    leitor_pdf = PdfReader(path_to_pdf)
    pag_conteudo = {}
    questoes = []
    #  Index de cada pagina in
    for index, pdf_pag in enumerate(leitor_pdf.pages):  
        pag_conteudo[index + 1] = pdf_pag.extract_text()
    # Remove primeira pagina que nao contem nenhuma questao
    pag_conteudo.pop(1) 
    # Inicia counter de paginas
    counter = 0
    for pagina, texto in pag_conteudo.items():
        questoes += texto.split("QUESTÃO")
        if f"CN - 1º dia I Caderno 3 - BRANCO - Página" in questoes[counter] or f"CH - 1º dia I Caderno 3 - BRANCO - Página" in questoes[counter]:
            questoes.pop(counter)
        counter += 1
    print(questoes[4])
        
    # Num questao = index + 1
    return questoes

Recupera_questoes_enem("/home/roberto/projects/enem10x/src/leitor_pdf/Enem_2012_dia1.pdf")