from django import forms
from .models import Todo_List


class Todo_ListForm(forms.ModelForm):
    class Meta:
        model=Todo_List
        fields=['author','new_todo'] 