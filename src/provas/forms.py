from django import forms
from materiais.models import Materia

# Forms down here

class ProvaChoose(forms.Form):
    QUESTOES_CHOICE = [(i, str(i)) for i in range(5,46)]
    MATERIAS_CHOICE = [(materia.id, str(materia)) for materia in (Materia.objects.all())]
    num_questoes = forms.ChoiceField(
        choices=QUESTOES_CHOICE,
        label='Quantas questoes voce quer de cada materia??',
        widget=forms.Select(),)
    materias = forms.MultipleChoiceField(
        choices=MATERIAS_CHOICE,
        widget=forms.CheckboxSelectMultiple,
        label='Quais materias?',
    )