from django.shortcuts import render, redirect, reverse
from main.models import ListModel
from main.forms import ListForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required


# def login_decorator(url):
#     def wrapper(func):
#         def wrapper_2(request, *args, **kwargs):
#             if request.user.is_authenticated:
#                 return func(request, *args, **kwargs)
#             else:
#                 return redirect(url)
#
#         return wrapper_2
#
#     return wrapper

@login_required(login_url=reverse_lazy('registration:login'))
def main_view(request):
    lists = ListModel.objects.filter(
        user=request.user,
    )

    context = {
        'lists': lists,
        'user_name': request.user.username
    }
    return render(request, 'index.html', context)

@login_required(login_url=reverse_lazy('registration:login'))
def create_view(request):

    if request.method == 'POST':
        form = ListForm({
            'user': request.user,
            'name': request.POST.get('name')
        })
        if form.is_valid():
            success_url = reverse('main:main')
            form.save()
            return redirect(success_url)
    else:
        form = ListForm()

    return render(request, 'new_list.html', {'form': form})

@login_required(login_url=reverse_lazy('registration:login'))
def edit_view(request, pk):
    list_ = ListModel.objects.get(id=pk)

    if request.method == 'POST':
        form = ListForm({
            'user': request.user,
            'name': request.POST.get('name')
        }, instance=list_)

        if form.is_valid():
            success_url = reverse('main:main')
            form.save()
            return redirect(success_url)
    else:
        form = ListForm(instance=list_)

    context = {
        'form': form,
        'pk': pk
    }

    return render(request, 'edit_list.html', context)
