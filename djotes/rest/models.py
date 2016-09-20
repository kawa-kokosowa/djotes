from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    contents = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,
                              related_name='notes')

    class Meta:
        ordering = ('created',)
