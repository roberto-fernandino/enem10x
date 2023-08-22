from materiais.funcs import define_image_path, define_ranking_conteudo_prova, retorna_tipos_prova
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
        verbose_name_plural = "Sub Materias"


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
    TIPOS_PROVA = [
        ('linguagens', 'Linguagens e suas Tecnologias'),
        ('matematica', 'Matemática e suas Tecnologias'),
        ('natureza', 'Ciências da Natureza'),
        ('humanas', 'Ciências Humanas'),
    ]

    enunciado = models.TextField(default=None, blank=False, null=True)
    
    imagem = models.ImageField(
        upload_to=define_image_path, null=True, blank=True, default=None
    )
    conteudo = models.ForeignKey(
        Conteudo, on_delete=models.DO_NOTHING, null=True, default=None, blank=True
    )
    opcoes = models.JSONField(null=True)
    opcao_correta = models.IntegerField(null=True, blank=True, default=None)
    nivel = models.ForeignKey(Nivel, on_delete=models.DO_NOTHING, null=True)
    tipo = models.CharField(default=None, blank=True, null=True, choices=TIPOS_PROVA, max_length=50)

    class Meta:
        verbose_name_plural = "Questoes"

    def __str__(self):
        return f"{self.conteudo}"

    def get_materia(self):
        return self.conteudo.sub_materia.materia


class ProvaRespondida(models.Model):
    questao = models.ForeignKey(Questao, on_delete=models.DO_NOTHING)
    resposta = models.IntegerField(default=None, null=True)
    acerto = models.BooleanField(default=None, blank=True, null=True)

    def set_acerto(self):
        if self.questao.opcao_correta == self.resposta:
            self.acerto = True
            self.save()
        else:
            self.acerto = False
            self.save()


    def get_conteudo(self):
        return self.questao.conteudo

    def get_tipo(self):
        return self.questao.tipo


class ProvaCompleta(models.Model):
    usuario = models.ForeignKey("usuarios.Account", on_delete=models.CASCADE)
    respostas = models.ManyToManyField(ProvaRespondida)
    nota = models.IntegerField(default=0)
    acertos = models.IntegerField(default=0)
    erros = models.IntegerField(default=0)
    ranking_piores_conteudos = models.JSONField(default=None, blank=True, null=True)
    ranking_melhores_conteudos = models.JSONField(default=None, blank=True, null=True)
    data_feita = models.DateTimeField(auto_now_add=True)
    acerto_dificuldade = models.JSONField(null=True)
    tipos = models.JSONField(null=True)

    def gera_relatorio(self):
        conteudos_errados = []
        conteudos_acertados = []
        acertos = 0
        erros = 0
        tipos = []
        acerto_questoes_faceis = 0
        acerto_questoes_medianas = 0
        acerto_questoes_dificeis = 0
        for resposta in self.respostas.all():
            if resposta.acerto:
                acertos += 1
                conteudos_acertados.append(resposta.questao.conteudo)
                if resposta.questao.nivel.nivel == 'Fácil':
                    acerto_questoes_faceis += 1
                elif resposta.questao.nivel.nivel == 'Média':
                    acerto_questoes_medianas += 1
                else:
                    acerto_questoes_dificeis += 1
            else:
                erros += 1
                conteudos_errados.append(resposta.questao.conteudo)
            tipos.append(resposta.questao.tipo)
            
        
        dificuldades_acerto_dict = {}
        dificuldades_acerto_dict[1] = acerto_questoes_faceis
        dificuldades_acerto_dict[2] = acerto_questoes_medianas
        dificuldades_acerto_dict[3] = acerto_questoes_dificeis


        self.acerto_dificuldade = dificuldades_acerto_dict
        self.ranking_piores_conteudos, self.ranking_melhores_conteudos = define_ranking_conteudo_prova(conteudos_acertados=conteudos_acertados, conteudos_errados=conteudos_errados)
        tipos = list(set(tipos))
        
        self.tipos = tipos
        self.erros = erros
        self.acertos = acertos
        self.save()
    
    def calcula_nota(self):
        pass
