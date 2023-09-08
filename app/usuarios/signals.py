from django.db.models.signals import post_save
from django.dispatch import receiver
from usuarios.models import Account

@receiver(post_save, sender=Account)
def manage_aluno_professor(sender, instance, **kwargs):
    from usuarios.models import Aluno, Professor
    try:
        aluno = Aluno.objects.get(usuario=instance)
        if not instance.is_aluno:
            aluno.delete()
    except Aluno.DoesNotExist:
        if instance.is_aluno:
            Aluno.objects.create(usuario=instance)
    try:
        professor = Professor.objects.get(usuario=instance)
        if not instance.is_professor:
            professor.delete()
    except Professor.DoesNotExist:
        if instance.is_professor:
            Professor.objects.create(usuario=instance)
