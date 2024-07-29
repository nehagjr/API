from rest_framework import serializers
from .models import Student

# Create your models here.
class StudentSerializer(serializers.Serializer):
    nm=serializers.CharField(max_length=20)
    city=serializers.CharField(max_length=20)
    age=serializers.IntegerField()

    def __str__(self):
        return self.nm