from django.shortcuts import render,HttpResponse
import io 
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import Student
from .serializers import StudentSerializer,TeacherSerializer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def student_dserialize(request):
    if request.method=='POST':
        data = request.body
        stream = io.BytesIO(data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'data created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    


@csrf_exempt

def teacher_dserialize(request):
    if request.method=='POST':
        data = request.body
        stream = io.BytesIO(data)
        python_data = JSONParser().parse(stream)
        serializer = TeacherSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'data created !'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_errors = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_errors,content_type='application/json')

   
    




