from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    title =models.CharField(max_length=50) 
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, related_name='notes', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    