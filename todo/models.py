from django.db import models
from datetime import datetime
from django.conf import settings
from django.contrib.auth import get_user_model
User = get_user_model()

class Todo_List(models.Model):
    author=models.ForeignKey(User,  on_delete=models.CASCADE) 
    new_todo=models.CharField(max_length=100)
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=datetime.now)


    def __str__(self):
        return self.new_todo 