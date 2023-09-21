from typing import Any, Optional
from django.contrib import admin
from django.db.models.fields.related import ForeignKey
from django.forms.models import ModelChoiceField
from django.http.request import HttpRequest
from materiais.models import Materia, Nivel, SubMateria, Conteudo, Questao, ProvaCompleta, ProvaRespondida, QuestaoRespondida, Simulado, OpcaoImagem
# Register your models here.


class NivelAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        "nivel",
        "peso",
    ]
    fieldsets = (("Nivel", {"fields": ["nivel", "peso"]}),)
    search_fields = ['nivel']
    list_display_links = ['nivel']
    ordering = ['id']
class SubMateriaAdmin(admin.ModelAdmin):
    list_display = [
        "nome",
        "materia",
    ]
    fieldsets = ((None, {"fields": ["nome", "materia"]}),)
    search_fields = ['nome', 'materia']
    

class MateriaAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        "nome",
    ]
    fieldsets = ((None, {"fields": ["nome"]}),)
    list_display_links = ['nome']
    search_fields = ['nome']
    ordering = ['id']

class ConteudoAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "nome",
        "sub_materia",
    ]
    fieldsets = (
        (
            None,
            {
                "fields": [
                    "nome",
                    "sub_materia",
                ]
            },
        ),
    )
    list_display_links = ['nome']

class QuestaoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        "identificador_unico",
        'nivel',
        'Materia',
        'Submateria',
        'Conteudo',
    ]
    fieldsets = (
       (None, {"fields": [
           'enunciado',
            'imagem_enunciado',
            'identificador_unico',
            'opcoes',
            'opcao_correta',
            'conteudo',
            'nivel',
            ]}),
    )
    ordering = ['id']
    list_filter = ['conteudo']
    list_display_links = ['identificador_unico']
    

    def Materia(self, obj):
        return [str(conteudo.sub_materia.materia) for conteudo in obj.conteudo.all()]
    def Conteudo(self, obj):
        return [str(conteudo) for conteudo in obj.conteudo.all()]
    def Submateria(self, obj):
        return [str(conteudo.sub_materia) for conteudo in obj.conteudo.all()]

@admin.register(OpcaoImagem)
class QuestoesImagemAdmin(admin.ModelAdmin):
    list_display = [
        'questao',
        'id',
        ]
    ordering = ['id']
    list_display_links = ['questao']
    fieldsets = (
        (None, {"fields": ['questao', 'imagem_a',  'imagem_b', 'imagem_c', 'imagem_d', 'imagem_e']}),
    )
'''class ProvaRespondidaAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'questao',
        'resposta',
        'acerto',
        'get_tipo',
        ]
    
    fieldsets = (
        (None, {"fields": ['questao', 'resposta', 'acerto']}),
    )

    def get_tipo(self, obj):
        return obj.get_tipo()
    
    get_tipo.admin_order_field = 'tipo'
    get_tipo.admin_short_description = 'Tipo'
    list_display_links = ['questao']'''
    



    
class ProvaCompletaAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'aluno',
        'data_feita',
        'nota',
        'simulado',
        ]
    fieldsets = (
        ('Informacao do Estudante', {"fields": ['aluno']}),
        ('Informacao da Prova', {"fields": ['simulado','nota', 'ranking_piores_conteudos', 'ranking_melhores_conteudos', ]}),
        ('Acertos e Erros', {"fields": ['acertos', 'erros', 'porcentagem_acerto', 'acerto_dificuldade']})

    )
    date_hierarchy = 'data_feita'

@admin.register(QuestaoRespondida)
class QuestoesRespondidasAdmin(admin.ModelAdmin):
    list_display = ['aluno', 'questao']

@admin.register(Simulado)
class SimuladoAdmin(admin.ModelAdmin):
    list_display = ['tipo']
    fieldsets = [
        (None, {"fields": ['tipo', 'materia']}),
    ]

admin.site.register(ProvaCompleta, ProvaCompletaAdmin)
admin.site.register(Conteudo, ConteudoAdmin)
admin.site.register(Nivel, NivelAdmin)
admin.site.register(Materia, MateriaAdmin)
admin.site.register(SubMateria, SubMateriaAdmin)
admin.site.register(Questao, QuestaoAdmin)
