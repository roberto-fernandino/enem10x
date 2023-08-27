from django import forms
from materiais.models import Materia, Simulado

# Forms down here

class ProvaChoose(forms.Form):
    QUESTOES_CHOICE = [(i, str(i)) for i in range(5,46) if i % 2 == 0]
    MATERIAS_CHOICE = [(materia.id, str(materia)) for materia in (Materia.objects.all())]
    SIMULADO_CHOICE = [(simulado.id, str(simulado)) for simulado in (Simulado.objects.all())]

    num_questoes = forms.ChoiceField(
        choices=QUESTOES_CHOICE,
        label='Quantas questoes voce quer de cada materia??',
        widget=forms.Select(),)
    simulados = forms.MultipleChoiceField(
        choices=SIMULADO_CHOICE,
        widget=forms.CheckboxSelectMultiple,
        label='Quais simulados?'
    )
    materias = forms.MultipleChoiceField(
        choices=MATERIAS_CHOICE,
        widget=forms.CheckboxSelectMultiple,
        label='Quais materias?',
    )

