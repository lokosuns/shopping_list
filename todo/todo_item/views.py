from django.shortcuts import render

data = {
    'lists': [
        {'name': 'Купить шариков', 'is_done': True},
        {'name': 'Заказать торт', 'is_done': False, 'date': '05.06.2020'},
        {'name': 'Разослать приглашения', 'is_done': False}
    ],
    'user_name': 'Anonim',
}


def list_view(request):
    context = data
    return render(request, 'list.html', context)
