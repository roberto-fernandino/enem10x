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
        verbose_name_plural = "Sub Materias"


class Conteudo(models.Model):
    nome = models.CharField(max_length=255)
    sub_materia = models.ForeignKey(
        SubMateria,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return f"{self.nome} - {self.sub_materia}"


class Tipo(models.Model):
    nome = models.CharField(max_length=80)

    def __str__(self) -> str:
        return f"{self.nome}"

class OpcaoImagem(models.Model):
    questao = models.OneToOneField("materiais.Questao", on_delete=models.CASCADE, related_name='opcoes_imagem')
    imagem_a = models.ImageField(upload_to=define_image_path, null=True, blank=True, default=None)
    imagem_b = models.ImageField(upload_to=define_image_path, null=True, blank=True, default=None)
    imagem_c = models.ImageField(upload_to=define_image_path, null=True, blank=True, default=None)
    imagem_d = models.ImageField(upload_to=define_image_path, null=True, blank=True, default=None)
    imagem_e = models.ImageField(upload_to=define_image_path, null=True, blank=True, default=None)
    
    
    def opcoes_imagem_dict(self):
        images = {
            'a': self.imagem_a.url if self.imagem_a else None,
            'b': self.imagem_b.url if self.imagem_b else None,
            'c': self.imagem_c.url if self.imagem_c else None,
            'd': self.imagem_d.url if self.imagem_d else None,
            'e': self.imagem_e.url if self.imagem_e else None,
        }
        return {key: img for key, img in images.items() if img}
    
    
    class Meta:
        verbose_name_plural = 'Opcoes com imagem'

class Questao(models.Model):
    enunciado = models.TextField(default=None, blank=False, null=True)
    imagem_enunciado = models.ImageField(
        upload_to=define_image_path, null=True, blank=True, default=None
    )
    conteudo = models.ManyToManyField(
        Conteudo, default=None, blank=True, related_name="questoes"
    )
    opcoes = models.JSONField(null=True)
    opcao_correta = models.CharField(
        null=False, blank=False, default=None, max_length=1
    )
    nivel = models.ForeignKey(
        Nivel, on_delete=models.DO_NOTHING, null=True, blank=True, default=None
    )

    identificador_unico = models.CharField(max_length=20, null=True, blank=True, unique=True)

    class Meta:
        verbose_name_plural = "Questoes"

    def __str__(self):
        return f"{self.id} - {self.identificador_unico}"



class ProvaRespondida(models.Model):
    '''Objeto temporario que armazena respostas de um usuario pra uma prova especifica
    Parametros:\n
        \t-usuario\n
        \t-questao\n
        \t-resposta\n
        \t-prova_completa\n
        \t-simulado'''
    aluno = models.ForeignKey("usuarios.Aluno", on_delete=models.CASCADE, null=True)
    questao = models.ForeignKey(Questao, on_delete=models.CASCADE)
    resposta = models.CharField(default=None, null=True, max_length=1, blank=True)
    acerto = models.BooleanField(default=None, blank=True, null=True)
    prova_completa = models.ForeignKey(
        "ProvaCompleta", on_delete=models.CASCADE, related_name="respostas", null=True
    )
    simulado = models.ForeignKey("materiais.Simulado", on_delete=models.DO_NOTHING, null=True, blank=True, default=None)

    def set_acerto(self):
        if self.questao.opcao_correta == self.resposta:
            self.acerto = True
        else:       
            self.acerto = False
        self.save()


class Simulado(models.Model):
    tipo = models.CharField(max_length=70)
    materia = models.ManyToManyField(Materia, default=None, blank=True)

    def __str__(self):
        return f"{self.tipo}"

class QuestaoRespondida(models.Model):
    """Tabela de questoes ja respondidas pra um usuario para nao utilizalas novamente ao criar provas, nao conta questoes que o usuario deixou em branco."""

    aluno = models.ForeignKey("usuarios.Aluno", on_delete=models.CASCADE)
    questao = models.ForeignKey(Questao, on_delete=models.CASCADE, null=True)

    @classmethod
    def set_questoes_ja_respondidas(cls, aluno):
        prova_respondidas = ProvaRespondida.objects.filter(aluno=aluno)
        for prova_respondida in prova_respondidas:
            questao = prova_respondida.questao
            cls.objects.create(aluno=aluno, questao=questao)


class ProvaCompleta(models.Model):
    """Modelo de prova completa onde o usuario podera ver suas provas completas"""
    aluno = models.ForeignKey("usuarios.Aluno", on_delete=models.CASCADE)
    nota = models.FloatField(default=0, null=True)
    acertos = models.IntegerField(default=0)
    erros = models.IntegerField(default=0)
    ranking_piores_conteudos = models.JSONField(default=None, blank=True, null=True)
    ranking_melhores_conteudos = models.JSONField(default=None, blank=True, null=True)
    data_feita = models.DateTimeField(auto_now_add=True)
    acerto_dificuldade = models.JSONField(null=True)

    def gera_relatorio(self):
        '''
        Gera um relatorio baseado no objeto provacompleta.
        '''
        conteudos_errados = []
        conteudos_acertados = []
        acertos = 0
        erros = 0
        acerto_questoes_faceis = 0
        acerto_questoes_medianas = 0
        acerto_questoes_dificeis = 0
        for resposta in self.respostas.filter(aluno=self.aluno):
            if resposta.acerto:
                acertos += 1
                for conteudo in resposta.questao.conteudo.all():
                    conteudos_acertados.append(conteudo)
                if resposta.questao.nivel.nivel == "Fácil":
                    acerto_questoes_faceis += 1
                elif resposta.questao.nivel.nivel == "Média":
                    acerto_questoes_medianas += 1
                else:
                    acerto_questoes_dificeis += 1
            else:
                erros += 1
                for conteudo in resposta.questao.conteudo.all():
                    conteudos_errados.append(conteudo)

        """{
            1: qtd_facil,
            2: qtd_medias,
            3: qtd dificil
        }"""
        dificuldades_acerto_dict = {}
        dificuldades_acerto_dict[1] = acerto_questoes_faceis
        dificuldades_acerto_dict[2] = acerto_questoes_medianas
        dificuldades_acerto_dict[3] = acerto_questoes_dificeis

        self.acerto_dificuldade = dificuldades_acerto_dict
        (
            self.ranking_piores_conteudos,
            self.ranking_melhores_conteudos,
        ) = define_ranking_conteudo_prova(
            conteudos_acertados=conteudos_acertados, conteudos_errados=conteudos_errados
        )
        
        # Salva tipos de prova, erros, acertos, materias

        self.erros = erros
        self.acertos = acertos
        self.save()

    def deleta_respostas(self):
        # Deleta todas as respostas do usuario em ProvaRespondida pra maior otimizacao
        self.respostas.filter(aluno=self.aluno).delete()

    def __str__(self):
        return f"{self.aluno} - {self.data_feita}"
