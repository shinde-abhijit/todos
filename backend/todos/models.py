from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class Todo(models.Model):
    TODO_STATUS = [
        ('', 'Status'),
        ('Completed', 'Completed'),
        ('Failed', 'Failed'),
        ('Pending', 'Pending'),
    ]

    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='user_todos')
    title = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=30, choices=TODO_STATUS, default='Pending', blank=False, null=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todo_created_by')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='todo_updated_by')

    def __str__(self):
        return f"Title - {self.title}, Added on - {self.created_at}"
    
    def clean(self):
        super().clean()
        if self.title.lower().strip() == self.description.lower().strip() and self.title.lower() == self.description.lower():
            raise ValidationError('Title and Description can not be same.')
    
    class Meta:
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'