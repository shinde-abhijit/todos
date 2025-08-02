from django.contrib import admin
from todos.models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = [
        'user', 
        'title', 
        'description', 
        'status', 
        'created_at', 
        'updated_at', 
    ]

    list_filter = [
        'user', 
        'title', 
        'description', 
        'status', 
        'created_at', 
        'updated_at', 
    ]

    search_fields = [
        'user', 
        'title', 
        'description', 
        'status', 
        'created_at', 
        'updated_at', 
    ]

    list_per_page = 100

admin.site.register(Todo, TodoAdmin)