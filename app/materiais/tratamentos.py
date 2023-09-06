# from materiais.funcs import replace_in_runs
import re
import docx

PATTERN_SUP_TAG = re.compile(r"(\d+(\.\d+)?x10\s*)(\-?\d+)")
PATTERN_CONTEUDO = re.compile(r"(.+?) / ?(.+?)\n")
PATTERN_ALTERNATIVAS = re.compile(r"\b(a|b|c|d|e)\)\s")
REPLACEMENT_ALTERNATIVAS = r"\1$ "
PATTERN_GAB = re.compile(r"Gab.*?([a-eA-E])", re.IGNORECASE)
REPLACEMENT_GAB = r"w$ \1"


# Remove when done
def docx_to_text(doc_obj):
    """
    Retorna o texto inteiro do .docx
    """
    full_text = []
    for paragraph in doc_obj.paragraphs:
        full_text.append(paragraph.text)
    return "\n".join(full_text)


# Remove when done
def replace_in_runs(paragraph, pattern, replacement):
    for run in paragraph.runs:
        if pattern.search(run.text):
            print(f"Encontrado em {run.text}")
            run.text = pattern.sub(replacement, run.text)


def trata_conteudos(texto_extraido_do_docx_em_string: str) -> str:
    """
    Aplica conteudos no texto e retorna o texto em str com as modificacoes.
    """
    texto_modificado = texto_extraido_do_docx_em_string
    matches = list(PATTERN_CONTEUDO.finditer(texto_extraido_do_docx_em_string))
    for match in matches:
        whole, conteudo, sub_conteudo = match.group(0), match.group(1), match.group(2)
        if len(conteudo) < 50 and len(sub_conteudo) < 50:
            replace = f"Conteudo: {conteudo} / {sub_conteudo};\n"
            texto_modificado = texto_modificado.replace(whole, replace, 1)
    return texto_modificado


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


def trata_alternativas(doc_obj, doc_path) -> None:
    """
    Salva arquivo com alternativas tratadas para extracao.
    """
    for para in doc_obj.paragraphs:
        replace_in_runs(para, PATTERN_ALTERNATIVAS, REPLACEMENT_ALTERNATIVAS)
    doc_obj.save(doc_path)


def replace_gab_runs_divided(paragraph):
    runs = paragraph.runs
    for i in range(len(runs) - 1):
        combined_text = runs[i].text + runs[i + 1].text
        if "Gab:" in combined_text:
            runs[i].text = combined_text.replace("Gab:", "w$")
            runs[i + 1].text = ""


def trata_gabs(doc_obj, doc_path):
    for para in doc_obj.paragraphs:
        replace_gab_runs_divided(para)
    doc_obj.save(doc_path)


class tratamento_geral_pra_extracao:
    def __init__(self, doc_obj, doc_path) -> None:
        self.doc_obj = doc_obj
        self.doc_path = doc_path

    def Tratamento(self):
        trata_gabs(self.doc_obj, self.doc_path)
        trata_alternativas(self.doc_obj, self.doc_path)

    def Tratamento_sup_tags(self):
        apply_sup_tags(self.doc_obj, self.doc_path)


doc_obj = docx.Document("app/leitores/questoesmat.docx")
tratamento = tratamento_geral_pra_extracao(
    doc_obj=doc_obj, doc_path="app/leitores/questoesmat.docx"
)

tratamento.Tratamento()
