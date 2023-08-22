from pathlib import Path
import os
from django.utils.text import slugify


def define_image_path(instance, filename: str) -> str:
    ext = os.path.splitext(filename)[1]
    filename = f'{slugify(instance.materia)}.{ext.lstrip(".")}'
    return Path(f"imagens/{filename}")


def define_ranking_conteudo_prova(conteudos_errados: list, conteudos_acertados: list):
    """Gera um ranking de conteudos mais errados, acertados respectivamente de uma prova especifica e os retorna no formato:
    tuple(ranking errados, ranking acertados)"""

    ranking = {}
    maior_contagem = 0
    for conteudo in conteudos_errados:
        ranking[conteudo] = ranking.get(conteudo, 0) + 1
        if ranking[conteudo] > maior_contagem:
            maior_contagem = ranking[conteudo]
    ranking_erradas = dict(
        sorted(ranking.items(), key=lambda item: item[1], reverse=True)
    )

    ranking = {}
    maior_contagem = 0
    for conteudo in conteudos_acertados:
        ranking[conteudo] = ranking.get(conteudo, 0) + 1
        if ranking[conteudo] > maior_contagem:
            maior_contagem = ranking[conteudo]

    ranking_certos = dict(
        sorted(ranking.items(), key=lambda item: item[1], reverse=True)
    )

    return (
        ranking_erradas,
        ranking_certos,
    )
