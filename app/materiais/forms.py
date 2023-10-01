from django import forms
from .models import GrupoConteudo, Conteudo
from django.core.exceptions import ValidationError


class GrupoConteudoForm(forms.ModelForm):
    class Meta:
        model = GrupoConteudo
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        conteudo_em_grupos = set(
            GrupoConteudo.objects.exclude(pk=self.instance.pk)
            .values_list("conteudos", flat=True)
            )
        if self.instance.pk is not None and self.instance.materia:
            self.fields['conteudos'].queryset = self.fields['conteudos'].queryset.exclude(id__in=conteudo_em_grupos)
            self.fields['conteudos'].queryset = self.fields['conteudos'].queryset.filter(sub_materia__materia=self.instance.materia)
        else:
            self.fields['conteudos'].queryset = self.fields['conteudos'].queryset.exclude(id__in=conteudo_em_grupos)
            
    def clean_conteudos(self):
        conteudos = self.cleaned_data.get('conteudos')
        conteudo_em_grupos = set(
            GrupoConteudo.objects.exclude(pk=self.instance.pk)
            .values_list("conteudos", flat=True)
            )
        for conteudo in conteudos:
            if conteudo in conteudo_em_grupos:
                raise ValidationError(f"O conteúdo '{conteudo}' já está em outro grupo."
                )
        return conteudos
