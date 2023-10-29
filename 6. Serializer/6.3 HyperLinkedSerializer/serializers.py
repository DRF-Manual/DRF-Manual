from rest_framework import serializers
from .models import Animal, Zoo

# test를 할 때 urls.py와 views.py까지 serializer에 맞는 코드로 적용하시길 바랍니다.

class ZooSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Zoo
        fields = '__all__'


class AnimalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Animal
        fields = ['url','id','name','info','zoo']

# How hyperlinked views are determined
# extra_kwargs
class AnimalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Animal
        fields = ['url', 'id', 'name', 'info', 'zoo']
        extra_kwargs = {
            'url': {'view_name': 'animal', 'lookup_field': 'name'},
            'zoo': {'lookup_field': 'zoo_name'}
        }

# Serializer field
class AnimalSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='animal',
        lookup_field='name'
    )
    zoo = serializers.HyperlinkedRelatedField(
        view_name='zoo-name',
        lookup_field='zoo_name',
        read_only=True
    )

    class Meta:
        model = Animal
        fields = ['url', 'id', 'name', 'info', 'zoo']

# Changing the URL field name
class AnimalSerializer(serializers.HyperlinkedModelSerializer):
    url_field_name = 'animal_url'
    class Meta:
        model = Animal
        fields = ['animal_url', 'id', 'name', 'info', 'zoo']
        extra_kwargs = {
            'animal_url': {'view_name': 'animal', 'lookup_field': 'name'},
            'zoo': {'lookup_field': 'zoo_name'}
        }