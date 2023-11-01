from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from materiais.models import Materia, SubMateria, GrupoConteudo, Conteudo, Questao
from decimal import Decimal
from django.conf import settings
from materiais.adcionaquestoes import adiciona_questoes


# Create your tests here.
class MateriaTestCase(TestCase):
    def setUp(self) -> None:
        self.materia = Materia.objects.create(nome="Biologia")

    def test_materia_name(self):
        self.assertEqual(self.materia.nome, "Biologia")


class SubMateriaTestCase(TestCase):
    def setUp(self) -> None:
        self.materia = Materia.objects.create(nome="Biologia")
        self.sub_materia = SubMateria.objects.create(
            nome="Citologia", materia=self.materia
        )

    def test_sub_materia_relation(self):
        self.assertEqual(self.materia, self.sub_materia.materia)

    def test_sub_materia_name(self):
        self.assertEqual(self.sub_materia.nome, "Citologia")


class ConteudoTestCase(TestCase):
    def setUp(self) -> None:
        self.materia = Materia.objects.create(nome="Biologia")
        self.sub_materia = SubMateria.objects.create(
            nome="Citologia", materia=self.materia
        )
        self.conteudo = Conteudo.objects.create(
            nome="Células Animais", sub_materia=self.sub_materia
        )

    def test_conteudo_name(self):
        self.assertEqual(self.conteudo.nome, "Células Animais")

    def test_conteudo_relation(self):
        self.assertEqual(self.conteudo.sub_materia, self.sub_materia)


class GrupoConteudoTestCase(TestCase):
    def setUp(self) -> None:
        self.materia = Materia.objects.create(nome="Matemática")
        self.sub_materia = SubMateria.objects.create(
            nome="Álgebra", materia=self.materia
        )
        self.conteudo = Conteudo.objects.create(
            nome="Frações", sub_materia=self.sub_materia
        )
        self.conteudo1 = Conteudo.objects.create(nome="Equações")

    def test_grupo_conteudo_creation(self):
        grupo_conteudo = GrupoConteudo.objects.create(
            materia=self.materia, proporcao=Decimal("0.5")
        )
        self.assertIsInstance(grupo_conteudo, GrupoConteudo)
        self.assertEqual(grupo_conteudo.proporcao, Decimal("0.5"))
        self.assertEqual(grupo_conteudo.materia, self.materia)

    def test_grupo_conteudo_relation(self):
        grupo_conteudo = GrupoConteudo.objects.create(
            materia=self.materia, proporcao=Decimal("0.5")
        )
        grupo_conteudo.conteudos.add(self.conteudo, self.conteudo1)
        self.assertEqual(grupo_conteudo.conteudos.count(), 2)
        self.assertIn(self.conteudo, grupo_conteudo.conteudos.all())
        self.assertIn(self.conteudo1, grupo_conteudo.conteudos.all())


class QuestaoTestCase(TestCase):
    def setUp(self) -> None:
        try:
            adiciona_questoes("../app/leitores/questoesbio.docx", "Biologia")
            self.questao_aleatoria = Questao.objects.order_by("?").first()
        except Exception as e:
            print(f"Error: {e}")

    def test_questao_script_and_creation(self):
        self.assertIsInstance(self.questao_aleatoria, Questao)

    def test_questao_relation(self):
        conteudos = self.questao_aleatoria.conteudo.all()
        for conteudo in conteudos:
            self.assertIsInstance(conteudo, Conteudo)

    def test_opcoes(self):
        opcoes = self.questao_aleatoria.opcoes
        opcao_correta = self.questao_aleatoria.opcao_correta
        self.assertIsInstance(opcoes, list)
        self.assertIsInstance(opcao_correta, str)
        for opcao in opcoes:
            self.assertIsInstance(opcao, str)
        self.assertIn(opcao_correta, ["A", "B", "C", "D", "E"])

    def test_identificador_unico(self):
        self.assertIsInstance(self.questao_aleatoria.identificador_unico, str)
