from rest_framework import serializers
from .models import Cats, Messages, Users


class ListCatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cats
        fields = '__all__'
        
        
class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cats
        fields = [
            'cat_name',
            'cat_age',
            'cat_color',
            'cat_breed'
        ]
        
        
class UserMessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = [
            'where_message',
            'message_name',
            'message_content'
        ]
        
        
class ListUserMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = '__all__'
        
        
class RegisterUsers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = [
            'username',
            'email', 
            'address',
            'password'
        ]