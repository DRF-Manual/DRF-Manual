from rest_framework import serializers
from .models import Animal


# Customizing multiple create
class AnimalListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        animals = [Animal(**item) for item in validated_data]
        return Animal.objects.bulk_create(animals)

class AnimalSerializer(serializers.Serializer):
    ...
    class Meta:
        list_serializer_class = AnimalListSerializer


# Customizing multiple update
class AnimalListSerializer(serializers.ListSerializer):
    def update(self, instance, validated_data):
        # Maps for id->instance and id->data item.
        animal_mapping = {animal.id: animal for animal in instance}
        data_mapping = {item['id']: item for item in validated_data}

        # Perform creations and updates.
        ret = []
        for animal_id, data in data_mapping.items():
            animal = animal_mapping.get(animal_id, None)
            if animal is None:
                ret.append(self.child.create(data))
            else:
                ret.append(self.child.update(animal, data))

        # Perform deletions.
        for animal_id, animal in animal_mapping.items():
            if animal_id not in data_mapping:
                animal.delete()

        return ret

class AnimalSerializer(serializers.Serializer):
    # We need to identify elements in the list using their primary key,
    # so use a writable field here, rather than the default which would be read-only.
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=10)
    info = serializers.CharField()

    class Meta:
        list_serializer_class = AnimalListSerializer