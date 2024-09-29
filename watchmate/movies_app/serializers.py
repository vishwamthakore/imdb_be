from rest_framework import serializers
from movies_app.models import Movie


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=200)
    is_active = serializers.BooleanField(default=True)
    
    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
    
    def update(self, instance, validated_data):    
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()
        return instance
    
    def validate_name(self, value):
        if len(value) <= 2:
            raise serializers.ValidationError("Name should be longer than 2 characters")
        return value
    
    def validate(self, data):
        if data.get("name") == data.get("description"):
            raise serializers.ValidationError("Name and description should be different")
        return data
    