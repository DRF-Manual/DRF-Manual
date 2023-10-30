from rest_framework.decorators import api_view
from rest_framework.views import APIView, status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Zoo, Animal
from .serializers import ZooSerializer, AnimalSerializer

@api_view(['GET'])
def zoo_list(request):
    zoos = Zoo.objects.all()
    serializer = ZooSerializer(zoos, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def new_animal(request):
    serializer = AnimalSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ZooList(APIView):
    def get(self, request):
        zoos = Zoo.objects.all()
        serializer = ZooSerializer(zoos, many=True)
        return Response(serializer.data)


class ZooDetail(APIView):
    def get(self, request, pk):
        zoo = Zoo.objects.get(pk=pk)
        serializer = ZooSerializer(zoo)
        return Response(serializer.data)


class AnimalList(APIView):
    def get(self, request):
        animals = Animal.objects.all()
        serializer = AnimalSerializer(animals, many=True)
        return Response(serializer.data)


class AnimalDetail(APIView):
    def get(self, request, birth_year):
        animals = Animal.objects.filter(birth_year=birth_year)
        serializer = AnimalSerializer(animals, many=True)
        return Response(serializer.data)


class AnimalName(APIView):
    def get(self, request, name):
        animal=Animal.objects.get(name=name)
        serializer=AnimalSerializer(animal)
        return Response(serializer.data) 


class ZooViewSet(ModelViewSet):
    queryset = Zoo.objects.all()
    serializer_class = ZooSerializer


class AnimalViewSet(ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer