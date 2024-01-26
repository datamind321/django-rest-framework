from rest_framework import serializers



# create serializers here 


# student
class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    email = serializers.CharField(max_length=100)
    password=serializers.CharField(max_length=20)


# teacher 
    
class TeacherSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    email = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=20)

