from rest_framework import serializers
from movies_app.models import Review, Movie, Platform

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=200)
    is_active = serializers.BooleanField(default=True)
    created_at = serializers.DateTimeField(required=False)
        
    # platform_name = serializers.CharField(source='platform.name', read_only=True)
    platform_id = serializers.IntegerField(write_only=True)
    
    reviews = ReviewSerializer(many=True, read_only=True)

    
    def create(self, validated_data):
        platformId = validated_data.pop("platform_id")
        platform = Platform.objects.get(id=platformId)
        return Movie.objects.create(platform = platform, **validated_data)
    
    def update(self, instance, validated_data):    
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.save()
        return instance
    
    # def validate_name(self, value):
    #     if len(value) <= 2:
    #         raise serializers.ValidationError("Name should be longer than 2 characters")
    #     return value
    
    # def validate(self, data):
    #     if data.get("name") == data.get("description"):
    #         raise serializers.ValidationError("Name and description should be different")
    #     return data

    
class PlatformSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=200)
    website = serializers.URLField(max_length=100)
    
    movie_set = MovieSerializer(many=True, read_only=True)
    
    
    def create(self, validated_data):
        return Platform.objects.create(**validated_data)
    
    def update(self, instance, validated_data):    
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.website = validated_data.get('website', instance.is_active)
        instance.save()
        return instance
    
    
    