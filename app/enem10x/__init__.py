from __future__ import absolute_import, unicode_literals

# from __future__ garante que caso alguma coisa do python2 seja executada ele use as strings
# do python3 e o import do python 3 para nao deixar aconteceer nenhum conflitoo
from .celery import app as celery_app

__all__  = ("celery_app",)

