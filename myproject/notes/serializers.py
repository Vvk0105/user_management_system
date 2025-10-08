from rest_framework import serializers
from .models import Note

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'user', 'title', 'description', 'attachment', 'created_at', 'modified_at']
        read_only_fields = ['user', 'created_at', 'modified_at']
