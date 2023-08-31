from django.db.models.functions import TruncDate
from materiais.models import ProvaCompleta, QuestaoRespondida
from usuarios.models import Notas, MediaGeral
from datetime import timedelta
from django.utils import timezone
from django.db.models.functions import ExtractMonth


def calcular_media(user):
    """Calcula medias e adciona em medias medias do usuario ao longo do tempo"""
    provas_completas = ProvaCompleta.objects.filter(usuario=user)

    # start counter
    total_notas = {
        "matematica": 0,
        "ciencias_natureza": 0,
        "linguagens": 0,
        "ciencias_humanas": 0,
    }

    total_provas = {
        "matematica": 0,
        "ciencias_natureza": 0,
        "linguagens": 0,
        "ciencias_humanas": 0,
    }

    for prova in provas_completas:
        tipo = prova.tipo
        total_notas[tipo] += prova.nota
        total_provas[tipo] += 1

    # Calcula Medias
    medias = {
        "matematica": total_notas["matematica"] / total_notas["matematica"]
        if total_provas
        else 0,
        "ciencias_natureza": total_notas["ciencias_natureza"]
        / total_notas["ciencias_natureza"]
        if total_provas
        else 0,
        "linguagens": total_notas["linguagens"] / total_notas["linguagens"]
        if total_provas
        else 0,
        "ciencias_humanas": total_notas["ciencias_humanas"]
        / total_notas["ciencias_humanas"]
        if total_provas
        else 0,
    }

    # Cria model com media geral do usuario

    MediaGeral.objects.create(
        usuario=user,
        media_matematica=medias["matematica"],
        media_ciencias_natureza=medias["ciencias_natureza"],
        media_linguagens=medias["linguagens"],
        media_ciencias_humanas=medias["ciencias_humanas"],
    )


def NotaChart(usuario):
    month_set = {
        1: "Jan",
        2: "Fev",
        3: "Mar",
        4: "Abr",
        5: "Mai",
        6: "Jun",
        7: "Jul",
        8: "Ago",
        9: "Set",
        10: "Out",
        11: "Nov",
        12: "Dez",
    }

    data_mat = []
    data_nat = []
    data_hum = []
    data_lin = []
    months_mat = []
    months_nat = []
    months_hum = []
    months_lin = []

    queryset = Notas.objects.filter(usuario=usuario).order_by("data_calculada")
    nota_mes = queryset.annotate(mes=ExtractMonth("data_calculada"))
    for nota in nota_mes:
        if nota.nota_matematica:
            data_mat.append(nota.nota_matematica)
            months_mat.append(month_set[nota.mes])
        if nota.nota_linguagens:
            data_lin.append(nota.nota_linguagens)
            months_lin.append(month_set[nota.mes])
        if nota.nota_ciencias_humanas:
            data_hum.append(nota.nota_ciencias_humanas)
            months_hum.append(month_set[nota.mes])
        if nota.nota_ciencias_natureza:
            data_nat.append(nota.nota_ciencias_natureza)
            months_nat.append(month_set[nota.mes])

    return (
        data_mat,
        data_nat,
        data_lin,
        data_hum,
        months_mat,
        months_nat,
        months_lin,
        months_hum,
    )


def NotaFilteredChart(usuario, months:int | None = None):
    '''
        Filtara as notas baseado no Select com AJAX no graph.js.\n
        \t Retorna: as datas filtradas de acordo com a quantidade de tempo que o usario escolheu.
    '''
    month_set = {
        1: "Jan",
        2: "Fev",
        3: "Mar",
        4: "Abr",
        5: "Mai",
        6: "Jun",
        7: "Jul",
        8: "Ago",
        9: "Set",
        10: "Out",
        11: "Nov",
        12: "Dez",
    }

    data_mat = []
    data_nat = []
    data_hum = []
    data_lin = []
    months_mat = []
    months_nat = []
    months_hum = []
    months_lin = []

    now = timezone.now()

    if months:
        start_date = now - timedelta(days=30 * months)
        queryset = Notas.objects.filter(usuario=usuario, data_calculada__gte=start_date).order_by("data_calculada")
    else:
        start_date = None
        queryset = Notas.objects.filter(usuario=usuario).order_by("data_calculada")
    
    
    nota_mes = queryset.annotate(mes=ExtractMonth("data_calculada"))
    for nota in nota_mes:
        if nota.nota_matematica:
            data_mat.append(nota.nota_matematica)
            months_mat.append(month_set[nota.mes])
        if nota.nota_linguagens:
            data_lin.append(nota.nota_linguagens)
            months_lin.append(month_set[nota.mes])
        if nota.nota_ciencias_humanas:
            data_hum.append(nota.nota_ciencias_humanas)
            months_hum.append(month_set[nota.mes])
        if nota.nota_ciencias_natureza:
            data_nat.append(nota.nota_ciencias_natureza)
            months_nat.append(month_set[nota.mes])

    return ({
        'data_mat': data_mat,
        'data_nat': data_nat,
        'data_lin': data_lin,
        'data_hum': data_hum,
        "months_mat":months_mat,
        "months_nat":months_nat,
        "months_lin":months_lin,
        "months_hum":months_hum,
    }
        
        
       
    )


def filtra_questoes_feitas(usuario, questao):
    return QuestaoRespondida.objects.filter(usuario=usuario, questao=questao)

def MediaQuery(usuario):
    '''
    Retorna media do usuario em matematica, natureza, linguagens, humanas nessa ordem'''
    medias = MediaGeral.objects.get(usuario=usuario)
    media_mat = medias.media_matematica
    media_nat = medias.media_ciencias_natureza
    media_lin = medias.media_linguagens
    media_hum = medias.media_ciencias_humanas
    return  media_mat, media_nat, media_lin, media_hum