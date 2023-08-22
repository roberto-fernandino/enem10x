from typing import Any, Optional
from django.contrib import admin
from django.db.models.fields.related import ForeignKey
from django.forms.models import ModelChoiceField
from django.http.request import HttpRequest
from materiais.models import *
# Register your models here.

class NivelAdmin(admin.ModelAdmin):
    list_display = [
        'nivel',
        'peso',
    ]
    fieldsets = (
        ("Nivel", {"fields": ['nivel', 'peso']}),
    )

class SubMateriaAdmin(admin.ModelAdmin):
    list_display = [
        'nome',
        'materia',
    ]
    fieldsets = (
        (None, {"fields": ['nome', 'materia']}),
    )
class MateriaAdmin(admin.ModelAdmin):
    list_display = [
        'nome',
    ]
    fieldsets = (
        (None, {"fields": ['nome']}),
    )

class ConteudoAdmin(admin.ModelAdmin):
    list_display = [
        'nome',
        'sub_materia',
    ]
    fieldsets = (
        (None, {"fields": ['nome', 'sub_materia',]}),
    )

class QuestoesAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nivel',
        'conteudo',
        'opcao_correta',
    ]
    fieldsets = (
        (None, {"fields": ['enunciado', 'imagem', 'conteudo', 'opcao_correta', 'nivel']}),
    )


admin.site.register(Conteudo, ConteudoAdmin)
admin.site.register(Nivel, NivelAdmin)
admin.site.register(Materia, MateriaAdmin)
admin.site.register(SubMateria, SubMateriaAdmin)
admin.site.register(Questao, QuestoesAdmin)
