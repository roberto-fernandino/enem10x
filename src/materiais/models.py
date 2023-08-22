from materiais.funcs import define_image_path, define_ranking_conteudo_prova
from django.db import models


# Create your models here.
class Nivel(models.Model):
    nivel = models.CharField(max_length=10)
    peso = models.FloatField()

    def __str__(self) -> str:
        return f"{self.nivel}"

    class Meta:
        verbose_name_plural = "Niveis"


class Materia(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.nome}"


class SubMateria(models.Model):
    nome = models.CharField(max_length=50)
    materia = models.ForeignKey(
        Materia, on_delete=models.CASCADE, default=None, null=True
    )

    def __str__(self) -> str:
        return f"{self.nome} - {self.materia}"

    class Meta:
        verbose_plural_name = "Sub Materias"


class Conteudo(models.Model):
    nome = models.CharField(max_length=30)
    sub_materia = models.ForeignKey(
        SubMateria,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return f"{self.nome} - {self.sub_materia}"


class Tipo(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.nome}"


class Questao(models.Model):
    enunciado = models.TextField(default=None, blank=False, null=True)
    imagem = models.ImageField(
        upload_to=define_image_path, null=True, blank=True, default=None
    )
    conteudo = models.ForeignKey(
        Conteudo, on_delete=models.DO_NOTHING, null=True, default=None
    )
    opcao_correta = models.CharField(max_length=1, null=True, blank=False, default=None)
    nivel = models.ForeignKey(Nivel, on_delete=models.DO_NOTHING, null=True)
    tipo = models.ForeignKey(Tipo, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name_plural = "Questoes"


class QuestoesProva(models.Model):
    questao = models.ForeignKey(Questao, on_delete=models.CASCADE)

    def get_tipo(self):
        return self.questao.tipo

    def get_materia(self):
        return self.questao.conteudo.sub_materia.materia

    class Meta:
        verbose_name_plural = "Questoes pra prova"


class ProvaRespondida(models.Model):
    questao = models.ForeignKey(Questao, on_delete=models.DO_NOTHING)
    resposta = models.CharField(max_length=1)
    acerto = models.BooleanField()

    def set_acerto(self):
        if self.questao.opcao_correta == self.resposta:
            self.acerto == True
        else:
            self.acerto == False

    def get_conteudo(self):
        return self.questao.conteudo

    def get_tipo(self):
        return self.questao.tipo


class ProvaCompleta(models.Model):
    usuario = models.ForeignKey("usuarios.Account", on_delete=models.CASCADE)
    respostas = models.ManyToManyField(ProvaRespondida)
    nota = models.IntegerField()
    acertos = models.IntegerField(default=0)
    erros = models.IntegerField(default=0)
    ranking_piores_conteudos = models.JSONField(default=None, blank=True, null=True)
    ranking_melhores_conteudos = models.JSONField(default=None, blank=True, null=True)
    tipo = models.CharField(max_length=12)

    def relatorio(self):
        conteudos_errados = []
        conteudos_acertados = []
        acertos = 0
        erros = 0
        for resposta in self.respostas.all():
            if resposta.acerto:
                acertos += 1
                conteudos_acertados.append(resposta.questao.conteudo)
            else:
                erros += 1
                conteudos_errados.append(resposta.questao.conteudo)
        (
            self.ranking_piores_conteudos,
            self.ranking_melhores_conteudos,
            self.conteudo_mais_errado,
            self.conteudo_mais_acertado,
        ) = define_ranking_conteudo_prova(
            conteudos_acertados=conteudos_acertados, conteudos_errados=conteudos_errados
        )
        self.erros = erros
        self.acertos = acertos
        self.save()
