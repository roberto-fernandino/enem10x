import docx


doc = docx.Document("/home/roberto/projects/enem10x/src/leitores/P002287.docx")

todo_texto = "\n".join([paragrafo.text for paragrafo in doc.paragraphs])

questoes = todo_texto.split("Questão")

for questao in questoes:
    print(questao)
