from rest_framework import serializers
from .models import Static_Message ,chat , new_Static_Message

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Static_Message
        fields = '__all__'
        
class ItemSerializer1(serializers.ModelSerializer):
    class Meta:
        model = chat
        fields = '__all__'
        
class ItemSerializer2(serializers.ModelSerializer):
    class Meta:
        model = new_Static_Message
        fields = '__all__'