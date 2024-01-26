from django.shortcuts import render,HttpResponse
from rest_framework.renderers import JSONRenderer
from .models import Student,Teacher
from .serializers import StudentSerializer,TeacherSerializer
from django.http import JsonResponse

# Create your views here.

def student_view(request):
    data = Student.objects.all()
    serializer = StudentSerializer(data,many=True)
    return JsonResponse(serializer.data,safe=False)
    #          ------------ OR ---------------------
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data,content_type='application/json')



def teacher_view(request):
    data = Teacher.objects.all()
    serializer = TeacherSerializer(data,many=True)
    return JsonResponse(serializer.data,safe=False) 
    

