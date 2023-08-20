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
        'nome'
    ]
    fieldsets = (
        (None, {"fields": ['nome']}),
    )
class MateriaAdmin(admin.ModelAdmin):
    list_display = [
        'nome',
        'submateria',
    ]
    fieldsets = (
        (None, {"fields": ['nome', 'submateria']}),
    )

class QuestoesAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'materia',
        'nivel',
        'get_submateria',
    ]
    def get_submateria(self, obj):
        return obj.materia.submateria.nome
    
    get_submateria.short_description = 'Submateria'

    '''def formfield_for_foreignkey(self, db_field: ForeignKey[Any], request: HttpRequest | None, **kwargs: Any) -> ModelChoiceField | None:
        kwargs["queryset"] = Materia.objects.select_related('submateria')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)'''

    fieldsets = (
        (None, {"fields": ['enunciado', 'imagem', 'opcoes', 'materia', 'opcao_correta', 'nivel']}),
    )

admin.site.register(Nivel, NivelAdmin)
admin.site.register(Materia, MateriaAdmin)
admin.site.register(SubMateria, SubMateriaAdmin)
admin.site.register(Questoes, QuestoesAdmin)
