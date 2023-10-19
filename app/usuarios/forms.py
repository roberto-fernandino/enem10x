from django import forms
from usuarios.models import Account, Turma
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField


# Form para criar novas contas
class AccountCreationForm(forms.ModelForm):
    """Objeto para criar contas no front-end e back-end"""

    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(
            attrs={
                "id": "email",
                "class": "form-control mb-3",
                "size": "40",
                "name": "email",
                "required": True,
                "placeholder": "nome@email.com* ",
            }
        ),
    )
    nome = forms.CharField(
        label="Nome",
        widget=forms.TextInput(
            attrs={
                "class": "form-control mb-3",
                "name": "nome",
                "maxlength": 30,
                "minlength": 3,
                "required": True,
                "placeholder": "Nome Completo*",
            }
        ),
    )
    telefone = forms.CharField(
        label="Telefone",
        widget=forms.TextInput(
            attrs={
                "class": "form-control mb-3",
                "name": "telefone",
                "maxlength": 13,
                "minlength": 11,
                "id": "telefone",
                "placeholder": "telefone*",
                "required": True,
            }
        ),
    )
    password1 = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(
            attrs={
                "id": "password1",
                "class": "form-control mb-3",
                "placeholder": "password*",
                "required": True,
            }
        ),
    )
    password2 = forms.CharField(
        label="Confirme Senha",
        widget=forms.PasswordInput(
            attrs={
                "id": "password2",
                "class": "form-control mb-3",
                "placeholder": "confirm password*",
                "required": True,
            }
        ),
    )
    data_nascimento = forms.DateField(
        label="Data de Nascimento",
        widget=forms.DateInput(
            attrs={
                "type": "date",
                "class": "form-control mb-3",
                "required": True,
            }
        ),
    )
    cpf = forms.CharField(
        label="cpf",
        widget=forms.TextInput(
            attrs={
                "class": "form-control mb-3",
                "placeholder": "cpf*",
                "id": "cpf",
                "required": True,
            }
        ),
    )
    is_newsletter = forms.BooleanField(
        label="Deseja receber NewsLetter?",
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                "class": "form-check-input",
                "id":"is_newsletter"
            },
        ),
        initial=True,
    )

    class Meta:
        model = Account
        fields = [
            "email",
            "telefone",
            "nome",
            "data_nascimento",
            "cpf",
            "is_newsletter",
        ]

    def clean_password2(self):
        "checa as duas senhas"
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]
        if password2 and password2 and (password1 != password2):
            self.add_error("password2", "As duas senhas nao conferem.")
        return password2

    def save(self, commit=True):
        """Cria os usuarios ao salvar"""
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password2"])
        if commit:
            user.save()
        return user


class AccountChangeForm(forms.ModelForm):
    """Objeto para atualizar dados no painel de admin"""

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Account
        fields = [
            "email",
            "password",
            "telefone",
            "nome",
            "data_nascimento",
            "cpf",
            "is_admin",
            "is_superuser",
            "is_aluno",
            "is_staff",
        ]


class CriarTurmaForm(forms.ModelForm):
    '''
    Form para criar turmas'''
    def __init__(self, professor, *args):
       super(CriarTurmaForm, self).__init__(*args)
       self.professor = professor



    nome = forms.CharField(
        max_length=180,
        label='Nome',
        widget=forms.TextInput(attrs={
            "class": "turma-creation-form",
            "placeholder": "nome"

        })
    )

    class Meta:
        model = Turma
        fields = [
            'nome',
        ]

    def save(self, commit=True):
        turma = super().save(commit=False)
        if commit:
            turma.save()
            turma.professores.add(self.professor)
        return turma
        