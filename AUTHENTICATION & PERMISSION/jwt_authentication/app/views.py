from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Student
from .serializers import StudentSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


# refresh token : http POST http://127.0.0.1:8000/varifytoken/ token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA2MTc4NDUxLCJpYXQiOjE3MDYxNzgwNDUsImp0aSI6IjdhOGZhZWM1OGE4NjQ2YTc4NjgwZGNkN2MyYTg2YzFiIiwidXNlcl9pZCI6Mn0.NwzmQGN5KrLQBWn1oW2q99AVDea0ODWBBpBL5Uo0Rl0"
# access token: http http://127.0.0.1:8000/studentapi/ 'Authorization:Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwNjI2NDQ0NSwiaWF0IjoxNzA2MTc4MDQ1LCJqdGkiOiIyMDczY2VkNGJiZDU0YTA1YWM4NDZkZWExMjk3ZGY1MyIsInVzZXJfaWQiOjJ9.j723WEUDWWZQpwvMOi7RhdbfzdKGAGfVBju5azGHMd0'

class StudentView(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes=[JWTAuthentication]
    permission_classes = [IsAuthenticated]



