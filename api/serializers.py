from rest_framework import serializers
from .models import Student
# class StudentSerializer(serializers.Serializer):
#     # id = serializers.IntegerField()
#     name = serializers.CharField(max_length=25)
#     roll = serializers.IntegerField()
#     city = serializers.CharField(max_length=100)
#
#     # Field Level Validation
#     # def validate_roll(self, value):
#     #     if value >= 200:
#     #         raise serializers.ValidationError('seat Full')
#     #     return value
#     # Object level validation
#     # def validate(self, data):
#     #     nm = data.get('name')
#     #     ct = data.get('city')
#     #     if nm.lower() == 'rohit' and ct.lower() != 'ranchi':
#     #         raise serializers.ValidationError('city must be Ranchi ')
#     #     return data
#
#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.roll = validated_data.get('roll', instance.roll)
#         instance.city = validated_data.get('city', instance.city)
#         instance.save()
#         return instance

# Model Serializer
class StudentSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(read_only=True)
    class Meta:
        model = Student
        fields = ['id', 'name', 'roll', 'city']

