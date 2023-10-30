from django.core.management.base import BaseCommand
from materiais.adcionaquestoes import adiciona_questoes
from pathlib import Path
import subprocess
from docx.opc.exceptions import PackageNotFoundError

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent


class Command(BaseCommand):
    help = "Adiciona questões no banco de dados"

    def add_arguments(self, parser):
        parser.add_argument(
            "--materia", type=str, help="Materia das questoes do .docx."
        )

    def handle(self, *args, **kwargs):
        materia = kwargs["materia"] if kwargs["materia"] else None
        if materia:
            try:
                script_path = "/scripts/zipextract.sh"
                nome_do_arquivo = input("Digite o nome do arquivo sem a ext '.docx' ")
                subprocess.run([script_path, nome_do_arquivo])
                arquivo = f"/app/leitores/{nome_do_arquivo}.docx"
                questoes_adcionadas = adiciona_questoes(
                    arquivo_path=arquivo, materia=materia
                )
                if questoes_adcionadas:
                    self.stdout.write(
                        self.style.SUCCESS(
                            f"{questoes_adcionadas} questões adicionadas com sucesso!"
                        )
                    )
                else:
                    self.stdout.write(self.style.ERROR("Nenhuma questao adcionada!"))
            except IndexError:
                self.stdout.write(
                    self.style.ERROR(
                        "Lembre-se de criar o arquivo com os identificadores unicos presente no arquivo."
                    )
                )
            except PackageNotFoundError:
                self.stdout.write(
                    self.style.ERROR(
                        f'Erro: arquivo {arquivo} nao encontrado na pasta "/app/leitores", certifique-se de que os arquivos pra extração estão presentes nesta pasta.'
                    )
                )
            except KeyboardInterrupt:
                self.stdout.write(
                    self.style.ERROR(f"\n[!] ctrl + c pressionado cancelando operação!")
                )
            except Exception as err:
                self.stdout.write(
                    self.style.ERROR(
                        f'[!] Erro não previsto favor me contactar e enviar o codigo de erro ->  "{err}"'
                    )
                )
        else:
            self.stdout.write(
                self.style.ERROR(
                    "Iformar uma materia eh obrigatorio. Informe uma materia com --materia <materia>."
                )
            )
