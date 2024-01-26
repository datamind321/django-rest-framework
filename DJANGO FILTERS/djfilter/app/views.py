from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Student
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication
from .serializers import StudentSerializers
from django_filters.rest_framework import DjangoFilterBackend,OrderingFilter
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny
from rest_framework import filters
# Create your views here.

class StudentView(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['name']
    # filter_backends = [SearchFilter]
    # search_fields = ['^name']
    permission_classes = []
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['name','email']
    ordering = ['-name']

    
    
    