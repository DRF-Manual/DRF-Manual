from rest_framework import serializers
from .models import Animal #구현된 Model

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ['id','name', 'info']
        
# Specifying which fields to include
class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = '__all__'

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        exclude = ['info']


# Specifying fiedls explicitly
class AnimalSerializer(serializers.ModelSerializer):
    medical_check = serializers.BooleanField()
    class Meta:
        model = Animal
        fields = ['id','name', 'info', 'medical_check']


# Specifying fiedls explicitly
class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = '__all__'
        read_only_fields = ['name', 'info']


#Additional keyword arguments
class CreateAnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ['name', 'info']
        extra_kwargs = {'info': {'required': False}}

    def create(self, validated_data):
        animal = Animal(
            name=validated_data['name'],
        )
        try:
            animal.info = validated_data['info']
        except Exception as e:
            animal.info = 'Good animal'
        animal.save()
        return animal