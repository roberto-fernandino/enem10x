from django.contrib import admin
from usuarios.models import Account, Notas, MediaGeral
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
        ("Informacao Geral", {"fields": ["email", "password", "last_login"]}),
        ("Informacao Pessoal", {"fields": ["cpf", "telefone", "data_nascimento", ]}),
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
    list_per_page = 50
    filter_horizontal = ['user_permissions']
    date_hierarchy = 'data_criacao'

class NotasAdmin(admin.ModelAdmin):
    list_display = [
        'usuario',
        'data_calculada',
        'nota_matematica',
        'nota_ciencias_natureza',
        'nota_linguagens',
        'nota_ciencias_humanas',

        ]
    


    fieldsets = (
        (None, {"fields": ['usuario',"nota_matematica", "nota_ciencias_natureza", "nota_ciencias_humanas", "nota_linguagens", "data_calculada"]}),
    )
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": [
                    "usuario",
                    "data_calculada",
                    "nota_matematica",
                    "nota_ciencias_natureza",
                    "nota_ciencias_humanas",
                    "nota_linguagens",
                ],
            },
        )
    ]
    search_fields = ['usuario']
    list_per_page = 50
    list_filter = ['data_calculada']
    date_hierarchy = 'data_calculada'

class MediaGeralAdmin(admin.ModelAdmin):
    list_display = [
        'usuario',
        'data_atualizada',
        'media_matematica',
        'media_ciencias_natureza',
        'media_linguagens',
        'media_ciencias_humanas',

        ]
    


    fieldsets = (
        (None, {"fields": ['usuario',"media_matematica", "media_ciencias_natureza", "media_ciencias_humanas", "media_linguagens"]}),
    )
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": [
                    "usuario",
                    "media_matematica",
                    "media_ciencias_natureza",
                    "media_ciencias_humanas",
                    "media_linguagens",
                ],
            },
        )
    ]
    search_fields = ['usuario']
    list_per_page = 50
    list_filter = ['data_atualizada']
    date_hierarchy = 'data_atualizada'
    

admin.site.register(Notas, NotasAdmin)
admin.site.register(MediaGeral, MediaGeralAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.unregister(Group)