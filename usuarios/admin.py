from django.contrib import admin
from usuarios.models import Account
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from usuarios.forms import AccountCreationForm, AccountChangeForm


# Register your models here.

class AccountAdmin(BaseUserAdmin):
    form = AccountChangeForm
    add_form = AccountCreationForm
    
    list_display = [
        "email",
        "nome",
        "last_login",
        "data_criacao",
        "is_admin",
        "is_aluno"
    ]


    fieldsets = (
        ("Informacao Geral", {"fields": ["email", "password"]}),
        ("Informacao Pessoal", {"fields": ["cpf", "telefone", "data_nascimento", "last_login"]}),
        ("Informacao Permissoes", {"fields": ["is_aluno", "is_admin", "is_staff", "is_superuser"]}),
    )
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": [
                    "email",
                    "nome",
                    "data_nascimento",
                    "cpf",
                    "password1",
                    "password2"
                ],
            },
        )
    ]

    list_filter = ['is_aluno', 'data_criacao']
    search_fields = ['email', 'nome']
    ordering = ['-last_login']
    filter_horizontal = ['user_permissions']

admin.site.register(Account, AccountAdmin)
admin.site.unregister(Group)