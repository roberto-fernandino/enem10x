from django.test import TestCase
from materiais.models import Materia
from .funcs import define_proporcao_conteudos_provas


# Create your tests here.
class DefineProporcaoConteudosProvasTeste(TestCase):
    databases = {'default', 'replica'}
    def test_define_proporcao_conteudos_provas(self):
        materia = Materia.objects.get(id=1)
        num_questoes = 10
        result = define_proporcao_conteudos_provas(materia, num_questoes)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, dict)