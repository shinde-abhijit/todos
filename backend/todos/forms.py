from django import forms
from todos.models import Todo

input_classes = (
    'w-full p-2 border border-gray-300 rounded-lg mt-1 mb-2 '
    'duration-300 '
)


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = [ 'title', 'description', 'status', ]
        labels = {
            'title':'Title', 
            'description':'Description', 
            'status':'Status', 
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'class':input_classes,
                'placeholder': 'Todo Title',
            }), 
            'description': forms.TextInput(attrs={
                'class':input_classes,
                'placeholder': 'Todo Description',
            }), 
            'status': forms.Select(attrs={
                'class':input_classes,
            }), 
        }
