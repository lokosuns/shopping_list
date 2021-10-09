from django.urls import path
from main.views import create_view, edit_view, delete_view, MainView, CreateView, main_view

app_name = 'main'

urlpatterns = [
    #path('', main_view, name='main'),
    path('', MainView.as_view(), name='main'),
    #path('create/', create_view, name='create'),
    path('create/', CreateView.as_view(), name='create'),
    path('delete/<int:pk>', delete_view, name='delete'),
    path('edit/<int:pk>', edit_view, name='edit'),
]