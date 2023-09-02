from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from datetime import datetime
from materiais.models import ProvaCompleta
from django.utils import timezone


# Create your models here.
class AccountManager(BaseUserManager):
    def create_user(
        self,
        email,
        nome,
        telefone,
        cpf,
        data_nascimento,
        data_criacao,
        password=None,
    ):
        # User managemnt
        if not email:
            raise ValueError("Email Obrigatorio.")
        if not nome:
            raise ValueError("Nome Obrigatorio.")
        if not telefone:
            raise ValueError("Telefone Obrigatorio.")
        if not data_nascimento:
            raise ValueError("Data de Nascimento Obrigatoria.")

        # User object creation
        user = self.model(
            email=self.normalize_email(email),
            nome=nome,
            telefone=telefone,
            password=password,
            data_nascimento=data_nascimento,
            data_criacao=data_criacao,
            cpf=cpf,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self,
        email,
        nome,
        telefone,
        cpf,
        data_nascimento,
        data_criacao=datetime.now(),
        password=None,
    ):
        # User managemnt
        if not email:
            raise ValueError("Email Obrigatorio.")
        if not nome:
            raise ValueError("Nome Obrigatorio.")
        if not telefone:
            raise ValueError("Telefone Obrigatorio.")
        if not data_nascimento:
            raise ValueError("Data de Nascimento Obrigatoria.")

        user = self.create_user(
            email=self.normalize_email(email),
            nome=nome,
            telefone=telefone,
            password=password,
            data_nascimento=data_nascimento,
            data_criacao=data_criacao,
            cpf=cpf,
        )
        user.set_password(password)
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.is_aluno = False
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    # Fields para usuario
    email = models.EmailField(max_length=255, unique=True)
    nome = models.CharField(max_length=30)
    cpf = models.CharField(max_length=15, unique=True, blank=False)
    telefone = models.CharField(max_length=15, default=None, blank=False, null=True)
    data_nascimento = models.DateField(blank=False, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    # Tags , account type.
    is_aluno = models.BooleanField(default=False, verbose_name="Aluno")
    is_professor = models.BooleanField(default=False, verbose_name="Professor")
    is_verified = models.BooleanField(default=False, verbose_name="Verificado")
    is_newsletter = models.BooleanField(default=True, verbose_name="Newsletter")

    # Permissions
    is_admin = models.BooleanField(default=False, verbose_name="admin")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # Sent object to AccountManager to create user
    objects = AccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["nome", "cpf", "telefone", "data_nascimento"]

    def __str__(self):
        return f"{self.nome}"

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label: str) -> bool:
        return True

    def esconde_cpf(self):
        return "*" * 7 + self.cpf[-5:-2] + "-" + self.cpf[-2] + self.cpf[-1]


class Notas(models.Model):
    usuario = models.ForeignKey(Account, on_delete=models.CASCADE)
    data_calculada = models.DateField(default=timezone.now, null=True, blank=False)
    nota_matematica = models.FloatField(default=None, null=True, blank=True)
    nota_ciencias_natureza = models.FloatField(default=None, null=True, blank=True)
    nota_linguagens = models.FloatField(default=None, null=True, blank=True)
    nota_ciencias_humanas = models.FloatField(default=None, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Notas provas"


class MediaGeral(models.Model):
    usuario = models.OneToOneField(Account, on_delete=models.CASCADE)
    data_atualizada = models.DateTimeField(auto_now=True)
    media_matematica = models.FloatField(default=None, null=True, blank=True)
    media_ciencias_natureza = models.FloatField(default=None, null=True, blank=True)
    media_linguagens = models.FloatField(default=None, null=True, blank=True)
    media_ciencias_humanas = models.FloatField(default=None, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Media Geral"


class Professor(models.Model):
    usuario = models.OneToOneField(Account, on_delete=models.CASCADE)
    alunos = models.IntegerField()
    total_alunos = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.usuario}"

    class Meta:
        verbose_name_plural = "Professores"

    def get_remaining_alunos(self):
        return (self.total_alunos - self.alunos)

class Aluno(models.Model):
    usuario = models.OneToOneField(Account, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.usuario}"


class Turma(models.Model):
    nome = models.CharField(max_length=180, unique=True)
    professores = models.ManyToManyField(Professor)
    alunos = models.ManyToManyField(Aluno)
    data_criada = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.nome}"

    def get_qtd_alunos(self):
        return self.alunos.all().count()