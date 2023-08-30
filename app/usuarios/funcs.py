from django.db.models.functions import TruncDate
from materiais.models import ProvaCompleta, QuestaoRespondida
from usuarios.models import MediaGeral
from datetime import datetime
from django.db.models.functions import ExtractMonth
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
    month_set = {
        1: 'Jan',
        2: 'Fev',
        3: 'Mar',
        4: 'Abr',
        5: "Mai",
        6: "Jun",
        7: 'Jul',
        8: 'Ago',
        9: 'Set',
        10: 'Out',
        11: 'Nov',
        12: 'Dez'
    }

    data_mat = []
    data_nat = []
    data_hum = []
    data_lin = []
    months_mat = []
    months_nat = []
    months_hum = []
    months_lin = []


    queryset = MediaGeral.objects.filter(usuario=usuario).order_by('data_calculada')
    media_mes = queryset.annotate(mes=ExtractMonth('data_calculada'))
    for media in media_mes:
        if media.media_matematica:
            data_mat.append(media.media_matematica)
            months_mat.append(month_set[media.mes])
        if media.media_linguagens:
            data_lin.append(media.media_linguagens)
            months_lin.append(month_set[media.mes])
        if media.media_ciencias_humanas:
            data_hum.append(media.media_ciencias_humanas)
            months_hum.append(month_set[media.mes])
        if media.media_ciencias_natureza:
            data_nat.append(media.media_ciencias_natureza)
            months_nat.append(month_set[media.mes])

    return data_mat, data_nat, data_lin, data_hum, months_mat, months_nat, months_lin, months_hum


def filtra_questoes_feitas(usuario, questao):
    return QuestaoRespondida.objects.filter(usuario=usuario, questao=questao)