from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    is_completed = serializers.BooleanField(required=False)
    class Meta:
        model = Todo
        fields = ['content', 'deadline', 'is_completed']
