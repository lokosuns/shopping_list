from django.template.defaulttags import register
from todo.settings import div_count


@register.filter
def get_count(lists):
    """
    Возвращает список - количество для генерации пустых блоков
    """

    return range(div_count - len(lists))

