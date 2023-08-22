from materiais.models import ProvaCompleta
from usuarios.models import MediaGeral

def calcular_media(user):
    # Recover all tests for that user
    provas_completas = ProvaCompleta.objects.filter(usuario=user)

    # start counter
    total_notas = {
        'matematica': 0,
        'ciencias_natureza': 0,
        'linguagens': 0,
        'ciencias_humanas': 0,
    }

    total_provas = {
        'matematica': 0,
        'ciencias_natureza': 0,
        'linguagens': 0,
        'ciencias_humanas': 0,
    }

    for prova in provas_completas:
        tipo = prova.tipo
        total_notas[tipo] += prova.nota
        total_provas[tipo] += 1

    # Calcula Medias
    medias = {
        'matematica': total_notas['matematica'] / total_notas['matematica'] if total_provas else 0,
        'ciencias_natureza': total_notas['ciencias_natureza'] / total_notas['ciencias_natureza'] if total_provas else 0,
        'linguagens': total_notas['linguagens'] / total_notas['linguagens'] if total_provas else 0,
        'ciencias_humanas': total_notas['ciencias_humanas'] / total_notas['ciencias_humanas'] if total_provas else 0,
    }    

    # Atualiza ou cria model com media geral do usuario

    MediaGeral.objects.update_or_create(
        usuario=user,
        defaults={
            'media_matematica': medias['matematica'],
            'media_ciencias_natureza': medias['ciencias_natureza'],
            'media_linguagens': medias['linguagens'],
            'media_ciencias_humanas': medias['ciencias_humanas']
        }
    )


