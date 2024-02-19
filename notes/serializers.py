
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Note, NoteChange

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'

class NoteChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteChange
        fields = '__all__'
