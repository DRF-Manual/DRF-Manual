from rest_framework import serializers
from .models import Zoo, Animal

class ZooSerializer(serializers.ModelSerializer):
    
     class Meta:
        model=Zoo 
        fields='__all__' 

class  AnimalSerializer(serializers.ModelSerializer):

     class Meta:
        model=Animal 
        fields='__all__'