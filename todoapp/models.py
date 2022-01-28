from django.db import models

class Todo(models.Model):
    todo_item = models.CharField(max_length=200)
    created = models.BooleanField(default=False)