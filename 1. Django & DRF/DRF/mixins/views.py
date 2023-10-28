# APIView
class ModelsAPIView(APIView):
    def get(self, request):
        models = Model.objects.all()
        serializer = ModelSerializer(models, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = ModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ModelAPIView(APIView):
    def get(self, request, pk):
        model = get_object_or_404(Model, id=pk)
        serializer = TaskDetailSerializer(model)
        return Response(serializer.data, status=status.HTTP_200_OK)


# mixins
from rest_framework import generics
from rest_framework import mixins

class ModelsAPIMixins(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer

    # get method 처리 함수(전체 모델)
    # mixins.ListModelMixin과 연결
    def get(self, request, *args, **kwargs):       
        return self.list(request, *args, **kwargs)

    # post method 처리 함수(전체 모델)
    # mixins.CreateModelMixin과 연결
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class ModelAPIMixins(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer

    # get method 처리 함수(특정 모델)
    # mixins.RetrieveModelMixin과 연결
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
