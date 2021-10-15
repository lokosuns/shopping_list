from django.urls import path
from main.views import edit_view, delete_view, MainView, CreateView

app_name = 'main'

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('create/', CreateView.as_view(), name='create'),
    path('delete/', delete_view, name='delete'),
    path('edit/<int:pk>', edit_view, name='edit'),
]
