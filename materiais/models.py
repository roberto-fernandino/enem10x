from materiais.funcs import define_image_path
from django.db import models

# Create your models here.
class Nivel(models.Model):
    nivel = models.CharField(max_length=10)
    peso = models.FloatField()

    def __str__(self) -> str:
        return f"{self.nivel}"

    class Meta:
        verbose_name_plural = 'Niveis'


class SubMateria(models.Model): 
    nome = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.nome}"

class Materia(models.Model):
    nome = models.CharField(max_length=50)
    submateria = models.ForeignKey(SubMateria, on_delete=models.DO_NOTHING)
    def __str__(self) -> str:
        return f"{self.nome} - {self.submateria}"

class Questoes(models.Model):
    enunciado = models.TextField(default=None, blank=False, null=True)
    imagem = models.ImageField(upload_to=define_image_path)
    materia = models.ForeignKey(Materia, on_delete=models.DO_NOTHING)
    opcoes =  models.JSONField()
    opcao_correta = models.CharField(max_length=1, null=True, blank=False, default=None)
    nivel = models.ForeignKey(Nivel, on_delete=models.DO_NOTHING)
    class Meta:
        verbose_name_plural = 'Questoes'
