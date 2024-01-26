from django.shortcuts import render
from .serializers import TeacherSerializer
from .models import Teacher
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView



class TeacherCreateList(ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeacherUpdateList(RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

