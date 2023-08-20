from pathlib import Path
import os
from django.utils.text import slugify


def define_image_path(instance, filename: str) -> str:
    ext = os.path.splitext(filename)[1]
    filename = f'{slugify(instance.materia)}.{ext.lstrip(".")}'
    return Path(f'imagens/{filename}')