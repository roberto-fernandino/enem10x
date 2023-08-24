from django.core.management.base import BaseCommand
from materiais.adcionaquestoes import adciona_questoes

class Command(BaseCommand):
    help = 'Adiciona questões no banco de dados'

    def handle(self, *args, **kwargs):
        arquivo = '/home/roberto/projects/enem10x/src/leitores/questions3.docx'
        adciona_questoes(arquivo)
        self.stdout.write(self.style.SUCCESS('Todas questões adicionadas com sucesso!'))
