from django.shortcuts import render
from main.models import ListModel
from todo_item.models import ItemModel

def item_view(request, pk):
    list_ = ListModel.objects.select_related('user').get(id=pk)
    list_items = ItemModel.objects.filter(list_model=list_)

    context = {
        'lists': list_items,
        'user_name': list_.user.username,
        'list_name': list_.name
    }

    return render(request, 'list.html', context)
