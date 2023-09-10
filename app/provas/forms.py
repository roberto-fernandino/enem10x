from collections.abc import Mapping
from typing import Any
from django import forms
from django.forms.utils import ErrorList
from materiais.models import Materia, Simulado

# Forms down here

class ProvaChoose(forms.Form):
    QUESTOES_CHOICE = [(i, str(i)) for i in range(5,46)]
    
    def __init__(self, *args, **kwargs) -> None:
        super(ProvaChoose, self).__init__(*args, **kwargs)
        self.fields['materias'].choices = [(materia.id, str(materia)) for materia in (Materia.objects.all())]
        self.fields['simulados'].choices = [(simulado.id, str(simulado)) for simulado in (Simulado.objects.all())]

    num_questoes = forms.ChoiceField(
        choices=QUESTOES_CHOICE,
        label='Quantas questoes voce quer de cada materia??',
        widget=forms.Select()
    )
    simulados = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        label='Quais simulados?',
        required=False,
    )
    materias = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        label='Quais materias?',
        required=False,
    )
    tipo_prova = forms.CharField(
        required=True
    )

