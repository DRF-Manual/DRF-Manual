from rest_framework import generics

class ModelsAPIGenerics(generics.ListCreateAPIView):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer

class ModelAPIGenerics(generics.RetrieveAPIView):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer