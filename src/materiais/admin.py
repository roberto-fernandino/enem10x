from typing import Any, Optional
from django.contrib import admin
from django.db.models.fields.related import ForeignKey
from django.forms.models import ModelChoiceField
from django.http.request import HttpRequest
from materiais.models import Materia, Nivel, SubMateria, Conteudo, Questao, ProvaCompleta, ProvaRespondida
# Register your models here.


class NivelAdmin(admin.ModelAdmin):
    list_display = [
        "nivel",
        "peso",
    ]
    fieldsets = (("Nivel", {"fields": ["nivel", "peso"]}),)
    search_fields = ['nivel']

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


class ConteudoAdmin(admin.ModelAdmin):
    list_display = [
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


class QuestoesAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'conteudo',
        'nivel',
        'opcao_correta',
    ]
    fieldsets = (
       (None, {"fields": ['enunciado', 'imagem', 'conteudo', 'opcao_correta', 'nivel']}),
    )
    list_display_links = ['conteudo']

class ProvaRespondidaAdmin(admin.ModelAdmin):
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
    list_display_links = ['questao']
    

class TipoAdmin(admin.ModelAdmin):
    list_display = ["nome"]
    fieldsets = (
        (
            None,
            {"fields": ["nome"]},
        ),
    )
    list_display_links = ['conteudo']

class ProvaRespondidaAdmin(admin.ModelAdmin):
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
    list_display_links = ['questao']
    

class ProvaCompletaAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'usuario',
        'nota',
        'acertos',
        'tipos',
        'data_feita',
        ]
    fieldsets = (
        ('Informacao do Estudante', {"fields": ['usuario']}),
        ('Informacao da Prova', {"fields": ['nota', 'ranking_piores_conteudos', 'ranking_melhores_conteudos', 'tipos']}),
        ('Acertos e Erros', {"fields": ['acertos', 'erros']})

    )
    date_hierarchy = 'data_feita'

admin.site.register(ProvaCompleta, ProvaCompletaAdmin)
admin.site.register(ProvaRespondida, ProvaRespondidaAdmin)
admin.site.register(Conteudo, ConteudoAdmin)
admin.site.register(Nivel, NivelAdmin)
admin.site.register(Materia, MateriaAdmin)
admin.site.register(SubMateria, SubMateriaAdmin)
admin.site.register(Questao, QuestoesAdmin)
