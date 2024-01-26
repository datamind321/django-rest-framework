from rest_framework import serializers
from .models import Student,Teacher


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    email = serializers.CharField(max_length=100)
    password=serializers.CharField(max_length=20)


    def create(self, validate_data):
        return Student.objects.create(**validate_data)
    


class TeacherSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    email = serializers.CharField(max_length=100)
    password=serializers.CharField(max_length=20)


    def create(self, validate_data):
        return Teacher.objects.create(**validate_data)