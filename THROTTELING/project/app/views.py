from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Student
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication
from .serializers import StudentSerializers
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle
from .customthrotteling import StudentUserRateThrottle



class StudentView(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [AnonRateThrottle,StudentUserRateThrottle]
    
