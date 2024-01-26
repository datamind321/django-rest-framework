from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Student,Teacher
from django.http import JsonResponse,HttpResponse
from .serializers import StudentSerializer,TeacherSerializer
import io
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import ValidationError
from rest_framework.decorators import authentication_classes,permission_classes
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

@api_view(['GET','POST','PUT','PATCH','DELETE'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticatedOrReadOnly])
@csrf_exempt
def student_api(request,id=None):
	if request.method=='GET':
		
		if id is not None:
			stu = Student.objects.get(id=id)
			serializer = StudentSerializer(stu)
			return Response(serializer.data)
		
		stu = Student.objects.all()
		serializer = StudentSerializer(stu,many=True)
		return Response(serializer.data)
	
	if request.method=='POST':
		serializer = StudentSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({'msg':'data created !'},status=status.HTTP_201_CREATED)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
		
	

	if request.method == 'PUT':
		id = request.data.get('id')
		stu = Student.objects.get(pk=id)
		print(stu)
		serializer = StudentSerializer(stu,data=request.data)
		print(serializer)
		if serializer.is_valid():
			serializer.save()
			print('I am done')
			return Response({'msg':'Complete data updated !'},status=status.HTTP_200_OK)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
	

	if request.method == 'PATCH':
		id = request.data.get('id')
		stu = Student.objects.get(pk=id)
		print(stu)
		serializer = StudentSerializer(stu,data=request.data)
		print(serializer)
		if serializer.is_valid():
			serializer.save()
			print('I am done')
			return Response({'msg':'Partially data updated !'},status=status.HTTP_200_OK)
		return Response(serializer.errors)
	
	if request.method == 'DELETE':
		
		stu = Student.objects.get(pk=id)
		stu.delete()
		return Response({'msg':'data deleted !'},status=status.HTTP_400_BAD_REQUEST)

	


	
	
	
		

# --------------------------------- Function Based API View -------------------------------------------

@api_view(['GET','POST','PUT','PATCH','DELETE'])	
@csrf_exempt
def teacher_api(request,id=None):
	if request.method=='GET':
		if id is not None:
			tech = Teacher.objects.get(pk=id)
			serializer = TeacherSerializer(tech)
			return Response(serializer.data)
		
		tech = Teacher.objects.all()
		serializer = TeacherSerializer(tech,many=True)
		return Response(serializer.data)
		
	
	if request.method=='POST':
		serializer = TeacherSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({'msg':'data created !'},status=status.HTTP_200_OK)
		return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
	

	if request.method=='PUT':
		id = request.data.get('id')
		tech = Teacher.objects.get(pk=id)
		serializer = TeacherSerializer(tech,data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({'msg':'Completely data updated !'},status=status.HTTP_200_OK)
		return Response(serializer.errors)

	if request.method=='PATCH':
		id = request.data.get('id')
		tech = Teacher.objects.get(pk=id)
		serializer = TeacherSerializer(tech,data=request.data,partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response({'msg':'Partially data updated !'},status=status.HTTP_200_OK)
		return Response(serializer.errors)


	if request.method=='DELETE':
		tech = Teacher.objects.get(pk=id)
		tech.delete()
		return Response({'msg':'data deleted !'},status=status.HTTP_200_OK)


	
# ------------------------- Class Based API View ----------------------------------------------

from rest_framework.views import APIView

class StudentAPIView(APIView):
	def get(self,request,id=None):
		if id is not None:
			try:
				stu = Student.objects.get(pk=id)
			except:
				return HttpResponse('<h3>Student Does not exists !</h3>')
				

			serializer = StudentSerializer(stu)
			return Response(serializer.data)
		    
		stu = Student.objects.all()
		serializer = StudentSerializer(stu,many=True)
		return Response(serializer.data)
	
	def post(self,request,format=None):
		serializer = StudentSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({'msg':'data added !'},status=status.HTTP_200_OK)
		
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
	
	def put(self,request,format=None):
		id = request.data.get('id')
		stu = Student.objects.get(pk=id)
		serializer = StudentSerializer(stu,data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({'msg':'completely data updated !'},status=status.HTTP_200_OK)
		
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
	

	def patch(self,request,format=None):
		id = request.data.get('id')
		stu = Student.objects.get(pk=id)
		serializer = StudentSerializer(stu,data=request.data,partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response({'msg':'partially data updated !'},status=status.HTTP_200_OK)
		
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
	
	def delete(self,request,id,format=None):
		stu = Student.objects.get(pk=id)
		stu.delete()
		return Response({'msg':'data deleted !'},status=status.HTTP_200_OK)
