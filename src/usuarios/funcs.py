from django.db.models.functions import TruncDate
from materiais.models import ProvaCompleta
from usuarios.models import MediaGeral
from datetime import datetime
def calcular_media(user):
    '''Calcula medias e adciona em medias medias do usuario ao longo do tempo'''
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

    # Cria model com media geral do usuario

    MediaGeral.objects.create(
        usuario=user,
        data_calculada = datetime.now(),
        media_matematica = medias['matematica'],
        media_ciencias_natureza = medias['ciencias_natureza'],
        media_linguagens =  medias['linguagens'],
        media_ciencias_humanas = medias['ciencias_humanas']
    )


def MediaChart(usuario):
    

    data_mat = [0]
    data_nat = [0]
    data_hum = [0]
    data_lin = [0]
    months = []

    queryset = MediaGeral.objects.filter(usuario=usuario)
    for media in queryset:
        data_mat.append(media.media_matematica)
        data_lin.append(media.media_linguagens)
        data_hum.append(media.media_ciencias_humanas)
        data_nat.append(media.media_ciencias_natureza)
        months.append(media.data_calculada)
    return data_mat, data_nat, data_lin, data_hum, months
