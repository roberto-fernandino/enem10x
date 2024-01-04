from django.contrib import admin
from usuarios.models import (
    Account,
    Notas,
    MediaGeral,
    Turma,
    Professor,
    Aluno,
    RankingConteudosErrados,
)
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
        "is_aluno",
        "is_professor",
        "id",
    ]

    fieldsets = (
        ("Informações Geral", {"fields": ["email", "password", "last_login"]}),
        (
            "Informações Pessoais",
            {
                "fields": [
                    "cpf",
                    "telefone",
                    "data_nascimento",
                ]
            },
        ),
        (
            "Tags",
            {
                "fields": [
                    "is_aluno",
                    "is_professor",
                    "is_verified",
                    "is_admin",
                    "is_staff",
                    "is_superuser",
                    "is_newsletter",
                ]
            },
        ),
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
                    "telefone",
                    "password1",
                    "password2",
                ],
            },
        )
    ]

    list_filter = ["is_aluno", "data_criacao"]
    search_fields = ["email", "nome"]
    ordering = ["-last_login"]
    list_per_page = 50
    filter_horizontal = ["user_permissions"]
    date_hierarchy = "data_criacao"


class NotasAdmin(admin.ModelAdmin):
    list_display = [
        "aluno",
        "data_calculada",
        "nota_matematica",
        "nota_ciencias_natureza",
        "nota_linguagens",
        "nota_ciencias_humanas",
    ]

    fieldsets = (
        (
            None,
            {
                "fields": [
                    "aluno",
                    "nota_matematica",
                    "nota_ciencias_natureza",
                    "nota_ciencias_humanas",
                    "nota_linguagens",
                    "data_calculada",
                ]
            },
        ),
    )
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": [
                    "aluno",
                    "data_calculada",
                    "nota_matematica",
                    "nota_ciencias_natureza",
                    "nota_ciencias_humanas",
                    "nota_linguagens",
                ],
            },
        )
    ]
    search_fields = ["aluno"]
    list_per_page = 50
    list_filter = ["data_calculada"]
    date_hierarchy = "data_calculada"


class MediaGeralAdmin(admin.ModelAdmin):
    list_display = [
        "aluno",
        "data_atualizada",
        "media_matematica",
        "media_ciencias_natureza",
        "media_linguagens",
        "media_ciencias_humanas",
    ]

    fieldsets = (
        (
            None,
            {
                "fields": [
                    "aluno",
                    "media_matematica",
                    "media_ciencias_natureza",
                    "media_ciencias_humanas",
                    "media_linguagens",
                ]
            },
        ),
    )
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": [
                    "aluno",
                    "media_matematica",
                    "media_ciencias_natureza",
                    "media_ciencias_humanas",
                    "media_linguagens",
                ],
            },
        )
    ]
    search_fields = ["aluno"]
    list_per_page = 50
    list_filter = ["data_atualizada"]
    date_hierarchy = "data_atualizada"


class TurmaAdmin(admin.ModelAdmin):
    list_display = ["nome", "id"]
    fieldssets = (
        ("Alunos", {"fields": ["alunos"]}),
        ("Professores", {"fields": ["professores"]}),
    )


class AlunoAdmin(admin.ModelAdmin):
    list_display = ["usuario"]
    fieldssets = (("Aluno", {"fields": ["usuario"]}),)


class ProfessorAdmin(admin.ModelAdmin):
    list_display = ["usuario", "alunos", "total_alunos"]
    fieldsets = (("Professor", {"fields": ["usuario", "alunos", "total_alunos"]}),)


class RankingGeralConteudoAdmin(admin.ModelAdmin):
    list_display = ["aluno", "tipo_simulado"]
    fieldsets = (
        ("Informação", {"fields": ["aluno", "tipo_simulado"]}),
        (
            "Conteudos",
            {
                "fields": [
                    "conteudo_1",
                    "conteudo_2",
                    "conteudo_3",
                    "conteudo_4",
                    "conteudo_5",
                ]
            },
        ),
    )


admin.site.register(RankingConteudosErrados, RankingGeralConteudoAdmin)
admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Turma, TurmaAdmin)
admin.site.register(Notas, NotasAdmin)
admin.site.register(MediaGeral, MediaGeralAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.unregister(Group)
