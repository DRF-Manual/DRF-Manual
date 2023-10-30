from rest_framework import serializers

# # Validators
# def name_is_alphabetic(value):
# 		if not(value.isalpha()):
# 			  raise serializers.ValidationError("Animal names must be alphabetic only.")

class AnimalSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=10)
    info = serializers.CharField()
    # # Validators
    # name = serializers.CharField(max_length=10, validators=[name_is_alphabetic])

    # # Meta Class validators
    # birth_at = serializers.DateField()
    # class Meta:
    #     # 이름과 생일이 똑같은 동물은 없습니다.
    #     validators = [
    #         UniqueTogetherValidator(
    #             queryset=Event.objects.all(),
    #             fields=['name', 'birth_at']
    #         )
    #     ]

    def create(self, validated_data):
        print('overriding create method')
        validated_data['name'] += '[1]'
        # Including extra context
        # print(self.context)
        return SerializerTest(**validated_data)
    
    def update(self, instance, validated_data):
        print('overriding update method')
        instance.values['name'] = validated_data.get('name', instance.values['name'])
        instance.values['info'] = validated_data.get('info', instance.values['info'])
        return instance
    
    # # Field-level validation
    # def validate_name(self, value):
    #     if not(value.isalpha()):
    #         raise serializers.ValidationError("Animal names must be alphabetic only.")
    #     return value
    
    # # Object-level validation
    # def validate(self, data):
    #     if len(data['name']) > len(data['info']):
    #         raise serializers.ValidationError("Info is too short")
    #     return data

class SerializerTest():
    def __init__(self,**values):
        self.values = values