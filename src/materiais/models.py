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
    conteudo = models.ManyToManyField(
        Conteudo,default=None, blank=True, related_name='questoes'
    )
    opcoes = models.JSONField(null=True)
    opcao_correta = models.CharField(null=False, blank=False, default=None, max_length=1)
    nivel = models.ForeignKey(Nivel, on_delete=models.DO_NOTHING, null=True, blank=True, default=None)
    tipo = models.CharField(default=None, blank=True, null=True, choices=TIPOS_PROVA, max_length=50)

    class Meta:
        verbose_name_plural = "Questoes"

    def __str__(self):
        return f"{self.id} - {self.nivel}"

    def get_materia(self):
        return self.conteudo.sub_materia.materia


class ProvaRespondida(models.Model):
    usuario = models.ForeignKey("usuarios.Account", on_delete=models.CASCADE, null=True)
    questao = models.ForeignKey(Questao, on_delete=models.CASCADE)
    resposta = models.CharField(default=None, null=True, max_length=1, blank=True)
    acerto = models.BooleanField(default=None, blank=True, null=True)
    prova_completa = models.ForeignKey("ProvaCompleta", on_delete=models.CASCADE, related_name='respostas', null=True)

    def set_acerto(self):
        print(f"questao: {self.questao.id} Opção correta: {self.questao.opcao_correta}, Resposta dada: {self.resposta}")
        if self.questao.opcao_correta == self.resposta:
            print("Acertou!")
            self.acerto = True
        else:
            print("Errou!")
            self.acerto = False
        self.save()


    def get_tipo(self):
        return self.questao.tipo
    

class QuestaoRespondida(models.Model):
    '''Tabela de questoes ja respondidas pra um usuario para nao utilizalas novamente ao criar provas, nao conta questoes que o usuario deixou em branco'''
    usuario = models.ForeignKey("usuarios.Account", on_delete=models.CASCADE)
    questao = models.ForeignKey(Questao, on_delete=models.CASCADE, null=True)
    
    @classmethod
    def set_questoes(cls, usuario):
        questoes_respondidas = ProvaRespondida.objetcs.filter(usuario=usuario)
        for questoes in questoes_respondidas:
            cls.objects.create(usuario=usuario, questao=questoes)


class ProvaCompleta(models.Model):
    '''Modelo de prova completa onde o usuario podera ver suas provas completas'''
    usuario = models.ForeignKey("usuarios.Account", on_delete=models.CASCADE)
    nota = models.FloatField(default=0, null=True)
    acertos = models.IntegerField(default=0)
    erros = models.IntegerField(default=0)
    ranking_piores_conteudos = models.JSONField(default=None, blank=True, null=True)
    ranking_melhores_conteudos = models.JSONField(default=None, blank=True, null=True)
    data_feita = models.DateTimeField(auto_now_add=True)
    acerto_dificuldade = models.JSONField(null=True)
    tipos = models.JSONField(null=True, default=None)
    
    def gera_relatorio(self):
        conteudos_errados = []
        conteudos_acertados = []
        acertos = 0
        erros = 0
        tipos = []
        acerto_questoes_faceis = 0
        acerto_questoes_medianas = 0
        acerto_questoes_dificeis = 0
        qtd_questoes = 0
        for resposta in self.respostas.filter(usuario=self.usuario):
            if resposta.acerto:
                acertos += 1
                for conteudo in resposta.questao.conteudo.all():
                    conteudos_acertados.append(conteudo)
                if resposta.questao.nivel.nivel == 'Fácil':
                    acerto_questoes_faceis += 1
                elif resposta.questao.nivel.nivel == 'Média':
                    acerto_questoes_medianas += 1
                else:
                    acerto_questoes_dificeis += 1
            else:
                erros += 1
                for conteudo in resposta.questao.conteudo.all():
                    conteudos_errados.append(conteudo)
            tipos.append(resposta.questao.tipo)
            
        '''{
            1: qtd_facil,
            2: qtd_medias,
            3: qtd dificil
        }'''
        dificuldades_acerto_dict = {}
        dificuldades_acerto_dict[1] = acerto_questoes_faceis
        dificuldades_acerto_dict[2] = acerto_questoes_medianas
        dificuldades_acerto_dict[3] = acerto_questoes_dificeis


        self.acerto_dificuldade = dificuldades_acerto_dict
        self.ranking_piores_conteudos, self.ranking_melhores_conteudos = define_ranking_conteudo_prova(conteudos_acertados=conteudos_acertados, conteudos_errados=conteudos_errados)
        tipos = list(set(tipos))
        # Salva tipos de prova, erros, acertos, materias
       
        self.tipos = tipos
        self.erros = erros
        self.acertos = acertos
        self.save()

    def deleta_respostas(self):
        # Deleta todas as respostas do usuario em ProvaRespondida pra maior otimizacao
        self.respostas.filter(usuario=self.usuario).delete()

    def __str__(self):
        return f"{self.usuario} - {self.data_feita}"
            

