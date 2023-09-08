from django.core.management.base import BaseCommand
from materiais.adcionaquestoes import adciona_questoes
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
print(str(BASE_DIR))

class Command(BaseCommand):
    help = 'Adiciona questões no banco de dados'

    def add_arguments(self,parser):
        parser.add_argument('--arquivo', type=str, help='Path para arquivo preparado no formato .docx com as questoes')
        parser.add_argument("--materia", type=str, help='Materia das questoes do .docx.')
        
    def handle(self, *args, **kwargs):
        arquivo = kwargs['arquivo'] if kwargs['arquivo'] else None
        materia = kwargs['materia'] if kwargs['materia'] else None
        if materia:
            try:
                adciona_questoes(arquivo_path=arquivo, materia=materia)
                self.stdout.write(self.style.SUCCESS('Todas questões adicionadas com sucesso!'))
            except IndexError:
                self.stdout.write(self.style.ERROR('Lembre-se de criar o arquivo com os identificadores unicos presente no arquivo, colocar os conteudos em todas as questoes, e transformar as imagens em png.'))
        else:
            self.stdout.write(self.style.ERROR('Iformar uma materia eh obrigatorio. Informe uma materia com --materia <materia>.'))

