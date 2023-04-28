from django.db import models
from django.contrib.auth import get_user_model


class Todo(models.Model):
    content = models.TextField()
    is_completed = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField()
    uid = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id} / {self.uid} / {self.content}'
