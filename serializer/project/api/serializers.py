from rest_framework import serializers
from .models import Student

# Create your models here.
# class StudentSerializer(serializers.Serializer):
#     nm=serializers.CharField(max_length=20)
#     city=serializers.CharField(max_length=20)
#     age=serializers.IntegerField()

#     def create(self, validated_data):
#         """
#         Create and return a new `Student` instance, given the validated data.
#         """
#         return Student.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.nm = validated_data.get('nm', instance.nm)
#         instance.city = validated_data.get('city', instance.city)
#         instance.age = validated_data.get('age', instance.age)
#         instance.save()
#         return instance

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields=["id","nm","city","age"]