from rest_framework import serializers
from .models import ToDo



class ToDoSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    completed = serializers.BooleanField()
    created_at = serializers.ReadOnlyField()
    deadline = serializers.DateTimeField()


class UpdateToDoSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200, required=False)
    completed = serializers.BooleanField(required=False)
    created_at = serializers.ReadOnlyField()
    deadline = serializers.DateTimeField(required=False)

    def update(self, instance: ToDo, validated_data: dict):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance



    
    