from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Student
from .serializers import StudentSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly



# generate token ways :

# 1. Using Admin Panel
# 2. Using Command Prompt : python manage.py drf_create_token <username>
# 3. By Exposing an API Endpoint :
# Step1 : pip install httpie
# step2 : Using this command to generate token :
# >> http POST http:127.0.0.1:8000/gettoken/ username = "your username" password= "your password"

# 4. Using Signals

# go to models.py 

# write an signal function when user create token automatically generated for specific user


# for authentication using token 

# >> http http://127.0.0.1:8000/studentapi/ 'Authorization:Token 4ac855acc9120ef083dfd07c6a473d2eba97a5ea'

# >> http -f POST http://127.0.0.1:8000/studentapi/ name=sam email=sam@gmail.com city=lucknow 'Authorization:Token 4ac855acc9120ef083dfd07c6a473d2eba97a5ea'

# >> http -f PUT http://127.0.0.1:8000/studentapi/5/ name=Kunal email=sam@gmail.com city=lucknow 'Authorization:Token 4ac855acc9120ef083dfd07c6a473d2eba97a5ea'


# >> http DELETE http://127.0.0.1:8000/studentapi/5/ 'Authorization:Token 4ac855acc9120ef083dfd07c6a473d2eba97a5ea'




class StudentView(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]