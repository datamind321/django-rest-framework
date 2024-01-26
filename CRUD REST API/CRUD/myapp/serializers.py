from rest_framework import serializers 
from .models import Student,Teacher



class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields = ['id','name','email','password']
    



class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id','name','email','password']

