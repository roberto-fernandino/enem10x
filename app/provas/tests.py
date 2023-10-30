from django.test import TestCase
from materiais.models import Materia, SubMateria, GrupoConteudo, Conteudo


# Create your tests here.
class MateriaTestCase(TestCase):
    def setUp(self) -> None:
        self.materia = Materia.objects.create(nome="Biologia")

    def testMateriaNome(self):
        self.assertEqual(self.materia.nome, "Biologia")


class SubMateriaTestCase(TestCase):
    def setUp(self) -> None:
        self.materia = Materia.objects.create(nome="Biologia")
        self.submateria = SubMateria.objects.create(
            nome="Citologia", materia=self.materia
        )

    def testSubMateria(self):
        self.assertEqual(self.materia, self.submateria.materia)
        self.assertEqual(self.submateria.nome, "Citologia")


class ConteudoTestCase(TestCase):
    def setUp(self) -> None:
        self.materia = Materia.objects.create(nome="Biologia")
        self.sub_materia = SubMateria.objects.create(
            nome="Citologia", materia=self.materia
        )
        self.conteudo = Conteudo.objects.create(
            nome="Células Animais", sub_materia=self.sub_materia
        )

    def testConteudo(self):
        self.assertEqual(self.conteudo.sub_materia, self.sub_materia)
        self.assertEqual(self.conteudo.nome, "Células Animais")
