from django import template


words = [
    'Сэм',
    'Сэма',
]

register = template.Library()

@register.filter()
def censor(value):
    res = ''
    for word in value.split():
        if word in words:
            res += word[0] + '*'*(len(word)-1) + ' '
        else:
            res += word + ' '
    return res[:-1]
