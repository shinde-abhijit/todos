from django.urls import path
from todos.views import (
    add_todo, todo_list, todo_details, update_todo, delete_todo,
    completed_todo_list, pending_todo_list, failed_todo_list, search_todos,  
)
urlpatterns = [
    path('list/', todo_list, name='todo_list'),
    path('add', add_todo, name='add_todo'),
    path('complete/', completed_todo_list, name='complete_todo_list'),
    path('pending/', pending_todo_list, name='pending_todo_list'),
    path('failed/', failed_todo_list, name='failed_todo_list'),
    path('search/', search_todos, name='search_todos'),
    path('details/<int:pk>/', todo_details, name='todo_details'),
    path('update/<int:pk>/', update_todo, name='update_todo'),
    path('delete/<int:pk>/', delete_todo, name='delete_todo'),
]
