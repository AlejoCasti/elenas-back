from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework import filters

import json

from .models import Task
from .serializers import TaskSerializer, MyTokenObtainPairSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createTask(request):
  user = request.user
  data = json.loads(request.body)
  Task.objects.create(title = data['title'], description = data['description'], status = data['status'], created_by = request.user)
  return Response('ok')

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateTask(request):
  user = request.user
  tasks = user.task_set.filter(id=request.data['id'])

  if len(tasks) > 0:
    task = Task.objects.get(id=request.data['id'])
    serializer = TaskSerializer(instance=task, data=request.data)
    if (serializer.is_valid()):
      serializer.save()
  else:
    return Response('Error')
  
  return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteTask(request, id):
  user = request.user
  tasks = user.task_set.filter(id=id).values()
  if len(tasks) > 0:
    Task.objects.filter(id=id).delete()
  else:
    return Response('Error')
  return Response('ok')

@api_view(['POST'])
def signUp(request):
  data = json.loads(request.body)
  User.objects.create_user(username = data['username'], password = data['password'])
  return Response('ok')

class ApiSearchTaskListView(ListAPIView):
  serializer_class = TaskSerializer
  filter_backends = [filters.SearchFilter]
  search_fields = ['description']

  def get_queryset(self):
    return Task.objects.filter(created_by=self.request.user)
