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
