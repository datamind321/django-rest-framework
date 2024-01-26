from django.shortcuts import render
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerialiser
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

class StudentViewSets(viewsets.ViewSet):
    def list(self,request):

        print('*******list*******')
        print('BaseName: ',self.basename)
        print('Action: ',self.action)
        print('DetailS ',self.detail)
        print('Suffix: ',self.suffix)
        print('Name: ',self.name)
        print('Description: ',self.description)

        stu = Student.objects.all()
        serializer = StudentSerialiser(stu,many=True)
        return Response(serializer.data)
    
    def retrieve(self,request,pk=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(pk=id)
            serializer = StudentSerialiser(stu)
            return Response(serializer.data)
        
        
    def create(self,request):
        print('*******Create*******')
        print('BaseName: ',self.basename)
        print('Action: ',self.action)
        print('DetailS ',self.detail)
        print('Suffix: ',self.suffix)
        print('Name: ',self.name)
        print('Description: ',self.description)
        serializer = StudentSerialiser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data created !'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    

    def update(self,request,pk=None):
        print('*******Update*******')
        print('BaseName: ',self.basename)
        print('Action: ',self.action)
        print('DetailS ',self.detail)
        print('Suffix: ',self.suffix)
        print('Name: ',self.name)
        print('Description: ',self.description)
        id=pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerialiser(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'completely data updated !'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    

    def partial_update(self,request,pk=None):
        print('*******Partial Update*******')
        print('BaseName: ',self.basename)
        print('Action: ',self.action)
        print('DetailS ',self.detail)
        print('Suffix: ',self.suffix)
        print('Name: ',self.name)
        print('Description: ',self.description)
        id=pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerialiser(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'partially data updated !'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    

    def destroy(self,request,pk=None):
        print('*******Destroy*******')
        print('BaseName: ',self.basename)
        print('Action: ',self.action)
        print('DetailS ',self.detail)
        print('Suffix: ',self.suffix)
        print('Name: ',self.name)
        print('Description: ',self.description)
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'data deleted !'},status=status.HTTP_200_OK)
    





# --------------------- Model View Sets -------------------------
    
class StudentModelViewSets(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerialiser

class StudentModelListViewSets(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerialiser   