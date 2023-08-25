from django import template


register = template.Library()

@register.filter
def opcao_em_letra(value):
    letras = 'a b c d e '.split()
    return letras[value]