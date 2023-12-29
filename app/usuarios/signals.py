from django.db.models.signals import post_save
from django.dispatch import receiver
from usuarios.models import Account, MediaGeral, CordenadorEscola
from materiais.models import ProvaCompleta
from celery import shared_task
from materiais.funcs import organiza_provas_por_tipo, atualiza_ranking_por_tipo


@shared_task(soft_time_limit=300, time_limit=420)
@receiver(post_save, sender=ProvaCompleta)
def atualiza_ranking_aluno_erradas(sender, instance, **kwargs):
    from usuarios.models import Aluno

    aluno = Aluno.objects.get(usuario=instance.aluno.usuario)
    simulados_tipo = organiza_provas_por_tipo(sender, aluno)
    for tipo, provas_list in simulados_tipo.items():
        atualiza_ranking_por_tipo(aluno, tipo, provas_list)


@shared_task
@receiver(post_save, sender=Account)
def manage_aluno_professor(sender: Account, instance, **kwargs):
    """
    ## Signal ativado quando uma compra foi confirmada e o usario recebeu tag de aluno ou professor.
    `Cria no banco de dados um Aluno ou um Professor apontando pro usuario.`
    """
    from usuarios.models import Aluno, Professor

    try:
        aluno = Aluno.objects.get(usuario=instance)
        if not instance.is_aluno:
            pass
            # Enviar email de conta assinatura expirada / conta cancelada.

    except Aluno.DoesNotExist:
        if instance.is_aluno:
            aluno = Aluno.objects.create(usuario=instance)
            media_geral, created = MediaGeral.objects.get_or_create(aluno=aluno)
            # Enviar email de ativacao de conta de aluno quando concluido.

    try:
        professor = Professor.objects.get(usuario=instance)
        if not instance.is_professor:
            professor.delete()
    except Professor.DoesNotExist:
        if instance.is_professor:
            Professor.objects.create(usuario=instance)
            # Enviar email de ativacao de conta de professor quando concluido.
    try:
        cordenador = CordenadorEscola.objects.get(usuario=instance)
        if not instance.is_cordenador:
            cordenador.delete()

    except CordenadorEscola.DoesNotExist:
        CordenadorEscola.objects.create(usuario=instance)
