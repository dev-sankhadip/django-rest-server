from rest_framework import serializers
from .models import App

class AddAppSerializer(serializers.ModelSerializer):

    class Meta:
        model=App
        fields='__all__'
    
    def create(self, validated_data):
        app=App.objects.create(**validated_data)
        return app