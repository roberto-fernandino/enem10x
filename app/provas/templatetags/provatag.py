from django import template


register = template.Library()

@register.filter
def opcao_em_letra(value):
    letras = ['a', 'b', 'c', 'd', 'e']
    return letras[value] if value is not None and 0 <= value < len(letras) else ''

@register.filter
def get_dictionary_item(dictionary, key):
    item = dictionary.get(key, None)
    return item

@register.filter
def imagefield_to_url(image_field):
    if image_field:
        return image_field.url
    return None

