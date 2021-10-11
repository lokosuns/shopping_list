from django.urls import path
from todo_item.views import item_view, create_view, delete_item_view, edit_item_view, is_done_item_view

app_name = 'item'

urlpatterns = [
    path('<int:pk>', item_view, name='item'),
    path('create/<int:pk>', create_view, name='create'),
    path('delete/<int:pk>', delete_item_view, name='delete'),
    path('edit/<int:pk>', edit_item_view, name='edit'),
    path('is_done/', is_done_item_view, name='is_done'),
]