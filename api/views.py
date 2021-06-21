import io
import json
from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
def student_detail(request, pk):
    stu = Student.objects.get(id=pk)
    serializer = StudentSerializer(stu)
    print(serializer.data)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data)

# Query Set -All Student Data

def studentList(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu, many=True)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type='application/json')
    print(serializer.data)
    return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def studentCreate(request):
    if request.method == "POST":
        json_data = request.bodyURL = ""
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Created ! '}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
# @csrf_exempt
# def studentApi(request):
#     if request.method == 'GET':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata  = JSONParser().parse(stream)
#         id = pythondata.get('id', None)
#         if id is not None:
#             stu = Student.objects.get(id=id)
#             serializer = StudentSerializer(stu)
#             json_data = JSONRenderer().render(serializer.data)
#             return HttpResponse(json_data, content_type='application/json')
#         stu = Student.objects.all()
#         serializer = StudentSerializer(stu, many=True)
#         json_data = JSONRenderer.render(serializer.data)
#         return HttpResponse(json_data, content_type='application/json')
#     if request.method == 'POST':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         serializer = StudentSerializer(data=pythondata)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg': 'Data Created'}
#             # json_data = JSONRenderer().render(res)
#             json_data = json.dumps(res)
#             return HttpResponse(json_data, content_type='application/json')
#
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type='application/json')
#
#     if request.method == 'PUT':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         id = pythondata.get('id')
#         stu = Student.objects.get(id=id)
#         serializer = StudentSerializer(stu, data=pythondata, partial=False)
#         # partial Update some field changed and petch means totally  update data  then can't write partial all data given required.
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg': 'Data Updated ! '}
#             # json_data = json.dumps(res)
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='application/json')
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type='application/json')
#     if request.method == 'DELETE':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         id = pythondata.get('id')
#         stu = Student.objects.get(id=id)
#         stu.delete()
#         res = {'msg': 'Data  has been Deleted'}
#         json_data = json.dumps(res)
#         json_data = JSONRenderer().render(res)
#         HttpResponse(json_data, content_type='application/json')

# Function Based APIVIEW

from rest_framework.decorators import  api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def studentApi(request):
   if request.method == 'GET':
       id = request.data.get('id')
       if id is not None:
           stu = Student.objects.get(id=id)
           serializer=StudentSerializer(stu)
           return Response(serializer.data)
       stu = Student.objects.all()
       serializer = StudentSerializer(stu, many=True, status=status.HTTP_200_OK)
       return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)

   if request.method == 'POST':
       serializer = StudentSerializer(data=request.data)
       if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created !'}, status=status.HTTP_201_CREATED)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   if request.method == 'PUT':
       id = request.data.get('id')
       stu = Student.objects.get(pk=id)
       serializer = StudentSerializer(stu, data=request.data, partial=True)
       if serializer.is_valid():
           serializer.save()
           return Response({'msg': 'Data Updated'})
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   if request.method == 'DELETE':
       id = request.data.get('id')
       if id is not None:
           stu = Student.objects.get(pk=id)
           stu.delete()
           return Response({'msg':'Data has been deleted'})
       return Response({'msg':"Id isn't available "})


# Function Based APIView
@api_view(['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def studentApi(request, pk=None):
   if request.method == 'GET':
       id = pk
       if id is not None:
           stu = Student.objects.get(id=id)
           serializer =  StudentSerializer(stu)
           return Response(serializer.data)
       stu = Student.objects.all()
       serializer = StudentSerializer(stu, many=True)
       return Response(serializer.data)

   if request.method == 'POST':
       serializer = StudentSerializer(data=request.data)
       if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created !'})
       return Response(serializer.errors)

   if request.method == 'PUT':
       id = pk
       stu = Student.objects.get(pk=id)
       serializer = StudentSerializer(stu, data=request.data, partial=True)
       if serializer.is_valid():
           serializer.save()
           return Response({'msg': 'Data Complete Updated'})
       return Response(serializer.errors)
   if request.method == 'PETCH':
       id = pk
       stu = Student.objects.get(pk=id)
       serializer = StudentSerializer(stu, data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response({'msg': 'Data partial Updated'})
       return Response(serializer.errors)


   if request.method == 'DELETE':
       id = pk
       if id is not None:
           stu = Student.objects.get(pk=id)
           stu.delete()
           return Response({'msg':'Data has been deleted'})
       return Response({'msg':"Id isn't available "})

# Class Based APIView
from rest_framework.views import APIView

class StudentAPI(APIView):
    def get(self, request, format=None, pk=None):

            id = pk
            if id is not None:
                stu = Student.objects.get(id=id)
                serializer = StudentSerializer(stu)
                return Response(serializer.data)
            stu = Student.objects.all()
            serializer = StudentSerializer(stu, many=True)
            return Response(serializer.data)
    def post(self, request, format=None):
            serializer = StudentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg': 'Data Created !'})
            return Response(serializer.errors)
    def put(self, request, format=None, pk=None):
            id = pk
            stu = Student.objects.get(pk=id)
            serializer = StudentSerializer(stu, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg': 'Data Complete Updated'})
            return Response(serializer.errors)

    def patch(self, request, format=None, pk=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data partial Updated'})
        return Response(serializer.errors)
    def delete(self, request, format=None, pk=None):
            id = pk
            if id is not None:
                stu = Student.objects.get(pk=id)
                stu.delete()
                return Response({'msg': 'Data has been deleted'})
            return Response({'msg': "Id isn't available "})
