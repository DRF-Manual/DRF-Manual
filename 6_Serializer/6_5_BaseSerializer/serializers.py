from rest_framework import serializers
from .models import Animal

# Read only BaseSerializer Class
class AnimalSerializer(serializers.BaseSerializer):
    # to_representation() 메서드 구현
    def to_representation(self, instance):
        return {
            'name': instance.name,
            'info': instance.info
        }

# Read - Write BaseSerializer Class
class AnimalSerializer(serializers.BaseSerializer):
    # to_internal_value() 메서드 구현
    # .is_valid() 사용 가능
    def to_internal_value(self, data):
        name = data.get('name')
        info = data.get('info')

        # data 유효성 검사 실행.
        if not name:
            # 잘못된 형식일 경우 serializers.ValidationError 발생.
            # '.errors' 속성으로 사용 가능
            raise serializers.ValidationError({
                'name': 'This field is required.'
            })
        if len(name) > 10:
            raise serializers.ValidationError({
                'name': 'May not be more than 10 characters.'
            })
        if not info:
            raise serializers.ValidationError({
                'info': 'This field is required.'
            })

        # 검증된 data return
        # '.valdated_data' 속성으로 사용 가능
        return {
            'name': name,
            'info': info
        }

    def to_representation(self, instance):
        return {
            'name': instance.name,
            'info': instance.info
        }

    # .save()를 사용하기 위해 .create() 구현
    def create(self, validated_data):
        return Animal.objects.create(**validated_data)