from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AnimalSerializer, ZooSerializer
from .models import Animal, Zoo


class ZooView(APIView):
    def get(self, request, pk):
        querySet = Zoo.objects.get(pk=pk)
        serializer = ZooSerializer(querySet, context={'request':None})
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class AnimalView(APIView):
    def get(self, request, pk):
        querySet = Animal.objects.get(pk=pk)
        # Absolute URL
        serializer = AnimalSerializer(querySet, context={'request':request})
        print(serializer.data)
        # Relative URL
        serializer = AnimalSerializer(querySet, context={'request':None})
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

# How hyperlinked views are determined
# extra_kwargs
# Serializer field
class ZooView(APIView):
    def get(self, request, name):
        querySet = Zoo.objects.get(name=name)
        serializer = ZooSerializer(querySet, context={'request':None})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class AnimalView(APIView):
    def get(self, request, name):
        querySet = Animal.objects.get(name=name)
        serializer = AnimalSerializer(querySet, context={'request':None})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
# Changing the URL field name
class ZooView(APIView):
    def get(self, request, zoo_name):
        querySet = Zoo.objects.get(name=zoo_name)
        serializer = ZooSerializer(querySet, context={'request':None})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class AnimalView(APIView):
    def get(self, request, name):
        querySet = Animal.objects.get(name=name)
        serializer = AnimalSerializer(querySet, context={'request':None})
        return Response(serializer.data, status=status.HTTP_200_OK)