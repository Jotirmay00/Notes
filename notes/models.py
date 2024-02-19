from django.db import models


from django.contrib.auth.models import User

class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_notes')
    shared_with = models.ManyToManyField(User, related_name='shared_notes', blank=True)

class NoteChange(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name='changes')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

