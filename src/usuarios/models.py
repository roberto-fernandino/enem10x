from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
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
    cpf = models.CharField(max_length=14, unique=True, blank=False)
    telefone = models.CharField(max_length=13, default=None, blank=False, null=True)
    data_nascimento = models.DateField(blank=False, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    is_aluno = models.BooleanField(default=True, verbose_name="Aluno")
    

    # Permissions
    is_admin = models.BooleanField(default=False, verbose_name='admin')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # Sent object to AccountManager to create user
    objects = AccountManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["nome", "cpf", "telefone", "data_nascimento"]

    def __str__(self):
        return f"{self.nome}"
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label: str) -> bool:
        return True
    
    def esconde_cpf(self):
        return "*" * 7 +  self.cpf[-5:-2] + '-' + self.cpf[-2] + self.cpf[-1]
    


    
class MediaGeral(models.Model):
    usuario = models.ForeignKey(Account, on_delete=models.CASCADE)
    data_calculada = models.DateField(default=timezone.now, null=True, blank=False)
    media_matematica = models.FloatField(default=0)
    media_ciencias_natureza = models.FloatField(default=0)
    media_linguagens = models.FloatField(default=0)
    media_ciencias_humanas = models.FloatField(default=0)
    class Meta:
        verbose_name_plural = 'Medias Gerais'

    