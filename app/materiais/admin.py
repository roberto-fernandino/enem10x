from typing import Any, Optional
from django.contrib import admin
from django.db.models.fields.related import ForeignKey
from django.forms.models import ModelChoiceField
from django.http.request import HttpRequest
from .forms import GrupoConteudoForm
from materiais.models import (
    Materia,
    Nivel,
    SubMateria,
    Conteudo,
    Questao,
    ProvaCompleta,
    ProvaRespondida,
    QuestaoRespondida,
    Simulado,
    OpcaoImagem,
    GrupoConteudo,
)
from random import choice

# Register your models here.


class NivelAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "nivel",
    ]
    fieldsets = (("Nivel", {"fields": ["nivel"]}),)
    search_fields = ["nivel"]
    list_display_links = ["nivel"]
    ordering = ["id"]


class SubMateriaAdmin(admin.ModelAdmin):
    list_display = [
        "nome",
        "materia",
    ]
    fieldsets = ((None, {"fields": ["nome", "materia"]}),)
    search_fields = ["nome", "materia"]


class MateriaAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "nome",
    ]
    fieldsets = ((None, {"fields": ["nome"]}),)
    list_display_links = ["nome"]
    search_fields = ["nome"]
    ordering = ["id"]


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
    list_display_links = ["nome"]


@admin.action(description="Adiciona niveis aleatorios pra questoes selecionadas.")
def adiciona_niveis_aleatorios(modeladmin, request, queryset):
    questoes_list = list(queryset.values_list("id", flat=True))
    niveis_list = [nivel for nivel in Nivel.objects.all()]
    for questao_id in questoes_list:
        Questao.objects.filter(id=questao_id).update(nivel=choice(niveis_list))


class QuestaoAdmin(admin.ModelAdmin):
    actions = [adiciona_niveis_aleatorios]
    list_display = [
        "id",
        "identificador_unico",
        "nivel",
        "Materia",
        "Submateria",
        "Conteudo",
    ]
    fieldsets = (
        (
            None,
            {
                "fields": [
                    "imagem_enunciado",
                    "identificador_unico",
                    "opcoes",
                    "opcao_correta",
                    "conteudo",
                    "nivel",
                ]
            },
        ),
    )
    ordering = ["id"]
    list_filter = ["conteudo", "conteudo__sub_materia__materia", "identificador_unico"]
    list_display_links = ["identificador_unico"]

    def Materia(self, obj):
        return [str(conteudo.sub_materia.materia) for conteudo in obj.conteudo.all()]

    def Conteudo(self, obj):
        return [str(conteudo) for conteudo in obj.conteudo.all()]

    def Submateria(self, obj):
        return [str(conteudo.sub_materia) for conteudo in obj.conteudo.all()]


@admin.register(OpcaoImagem)
class QuestoesImagemAdmin(admin.ModelAdmin):
    list_display = [
        "questao",
        "id",
    ]
    ordering = ["id"]
    list_display_links = ["questao"]
    list_filter = ["questao"]
    fieldsets = (
        (
            None,
            {
                "fields": [
                    "questao",
                    "imagem_a",
                    "imagem_b",
                    "imagem_c",
                    "imagem_d",
                    "imagem_e",
                ]
            },
        ),
    )


"""class ProvaRespondidaAdmin(admin.ModelAdmin):
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
    list_display_links = ['questao']"""


class ProvaCompletaAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "aluno",
        "data_feita",
        "simulado",
    ]
    fieldsets = (
        ("Informacao do Estudante", {"fields": ["aluno"]}),
        (
            "Informacao da Prova",
            {
                "fields": [
                    "simulado",
                    "ranking_piores_conteudos",
                    "ranking_melhores_conteudos",
                ]
            },
        ),
        (
            "Acertos e Erros",
            {
                "fields": [
                    "acertos",
                    "erros",
                    "porcentagem_acerto",
                    "acerto_dificuldade",
                ]
            },
        ),
    )
    date_hierarchy = "data_feita"


@admin.register(QuestaoRespondida)
class QuestoesRespondidasAdmin(admin.ModelAdmin):
    list_display = ["aluno", "questao"]


@admin.register(Simulado)
class SimuladoAdmin(admin.ModelAdmin):
    list_display = ["tipo"]
    fieldsets = [
        (None, {"fields": ["tipo", "materia", "valor"]}),
    ]


@admin.register(GrupoConteudo)
class GrupoConteudoAdmin(admin.ModelAdmin):
    form = GrupoConteudoForm
    filter_horizontal = ["conteudos"]
    list_display = ["id", "materia", "conteudo", "proporcao"]
    fieldsets = ((None, {"fields": ["materia", "proporcao", "conteudos"]}),)

    def conteudo(self, obj):
        return [conteudo for conteudo in obj.conteudos.all()]


admin.site.register(ProvaCompleta, ProvaCompletaAdmin)
admin.site.register(Conteudo, ConteudoAdmin)
admin.site.register(Nivel, NivelAdmin)
admin.site.register(Materia, MateriaAdmin)
admin.site.register(SubMateria, SubMateriaAdmin)
admin.site.register(Questao, QuestaoAdmin)
