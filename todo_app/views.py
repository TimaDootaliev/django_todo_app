from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet


from .serializers import ToDoSerializer, UpdateToDoSerializer
from .models import ToDo

@api_view(['GET'])
def get_todos(request: Request) -> Response:
    print(request)
    queryset = ToDo.objects.all()
    serializer = ToDoSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_todo(request: Request) -> Response:
    print(request)
    serializer = ToDoSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    todo = ToDo.objects.create(**serializer.data)
    todo.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PATCH'])
def update_todo(request: Request, pk) -> Response:
    try:
        todo = ToDo.objects.get(pk=pk)
    except ToDo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = UpdateToDoSerializer(todo, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def delete_todo(request: Request, pk) -> Response:
    try:
        todo = ToDo.objects.get(pk=pk).delete()
        return Response({'msg': 'ToDo Successfully Delete'})
    except ToDo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

