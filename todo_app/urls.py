from django.urls import path

from .views import get_todos, create_todo, update_todo, delete_todo

urlpatterns = [
    path('todos/', get_todos, name='all-todos'),
    path('create-todo/', create_todo, name='create-todo'),
    path('update-todo/<int:pk>/', update_todo, name='update-todo'),
    path('delete-todo/<int:pk>/', delete_todo, name='delete-todo'),
]