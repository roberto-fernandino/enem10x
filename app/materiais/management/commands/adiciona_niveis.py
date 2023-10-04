from materiais.models import Nivel
from django.core.management.base import BaseCommand, CommandParser

class Command(BaseCommand):
    help = 'Adicina X niveis (--numero X) automaticamente no banco de dados.'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('--numero', type=int, help='Quantidade de niveis.')

    def handle(self, *args, **kwargs):
        num_niveis = kwargs['numero'] if kwargs['numero'] else None
        if num_niveis:
            try:
                for nivel in range(1, num_niveis+1):
                    Nivel.objects.create(nivel=nivel)
                self.stdout.write(self.style.SUCCESS(f'[*] {num_niveis} adicionados com sucesso!'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'[!] ERRO: ({e}.)'))    
        else:
            self.stdout.write(self.style.ERROR('[!] ERRO informe o numero de niveis.')) 