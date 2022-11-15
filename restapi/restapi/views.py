from .models import Estagiario, Setor
from django.http import JsonResponse
from .serializers import EstagiarioSerializer, SetorSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def estagiarios_list(request):
    if request.method == 'GET':
        estagiario = Estagiario.objects.all()
        serializer = EstagiarioSerializer(estagiario, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = EstagiarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def estagiarios_detail(request, id):

    try:
        estagiario = Estagiario.objects.get(pk=id)
    except Estagiario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = EstagiarioSerializer(estagiario)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = EstagiarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        estagiario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Setores
@api_view(['GET', 'POST'])
def setores_list(request):
    if request.method == 'GET':
        setor = Setor.objects.all()
        serializer = SetorSerializer(setor, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = SetorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def setores_detail(request, id):

    try:
        setor = Setor.objects.get(pk=id)
    except Setor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = SetorSerializer(setor)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SetorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        setor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        