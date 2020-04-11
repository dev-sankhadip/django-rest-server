from rest_framework import serializers, generics

from .models import User

class AddUser(serializers.ModelSerializer):
    
    class Meta:
        model=User
        fields=('uid','name','email','password')

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        return user


class RetrieveUsers(serializers.ModelSerializer):

    class Meta:
        model=User
        fields='__all__'



class UpdateUser(serializers.ModelSerializer):

    class Meta:
        model=User
        fields='__all__'

    def update(self, instance, validated_data):
        instance.uid=validated_data.get('uid', instance.uid)
        instance.email=validated_data.get('email', instance.email)
        instance.name=validated_data.get('name', instance.name)
        instance.password=validated_data.get('password', instance.password)
        instance.save()
        return instance

