from django.core.management.base import BaseCommand
from materiais.adcionaquestoes import adiciona_questoes
from pathlib import Path
import subprocess

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
print(str(BASE_DIR))

class Command(BaseCommand):
    help = 'Adiciona questões no banco de dados'

    def add_arguments(self, parser):
        parser.add_argument('--arquivo', type=str, help='Path para arquivo preparado no formato .docx com as questoes')
        parser.add_argument("--materia", type=str, help='Materia das questoes do .docx.')
        
    def handle(self, *args, **kwargs):
        arquivo = kwargs['arquivo'] if kwargs['arquivo'] else None
        materia = kwargs['materia'] if kwargs['materia'] else None
        if materia:
            try:
                questoes_adcionadas = adiciona_questoes(arquivo_path=arquivo, materia=materia)
                if questoes_adcionadas:
                    self.stdout.write(self.style.SUCCESS(f'{questoes_adcionadas} questões adicionadas com sucesso!'))
                else:
                    self.stdout.write(self.style.ERROR('Nenhuma questao adcionada!'))
            except IndexError:
                self.stdout.write(self.style.ERROR('Lembre-se de criar o arquivo com os identificadores unicos presente no arquivo.'))
            except FileNotFoundError:
                self.stdout.write(self.style.ERROR('Erro, os arquivos de imagem da questao estao em um formato esquisito.'))
                self.stdout.write(self.style.SUCCESS('Porem ja pensei nisso e fiz um script que transforma eles em png e os extrai normalmente.'))
                script_path = "/home/roberto/projects/enem10x/scripts/zipextract.sh"
                nome_do_arquivo = input("Digite o nome do arquivo sem a ext '.docx' ")
                subprocess.run([script_path, nome_do_arquivo])
                questoes_adcionadas = adiciona_questoes(arquivo_path=arquivo, materia=materia)

        else:
            self.stdout.write(self.style.ERROR('Iformar uma materia eh obrigatorio. Informe uma materia com --materia <materia>.'))

