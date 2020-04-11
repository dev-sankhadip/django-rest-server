from rest_framework import status, viewsets
from rest_framework import status
from rest_framework.response import Response
from .models import App
from .serializer import AddAppSerializer

class AppViewSet(viewsets.ModelViewSet):

    def list(self, request, *args, **kwargs):
        serializer_class=self.get_serializer(data=request.data);
        return Response(status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    def get_serializer_class(self):
        if self.request.method=='GET':
            return AddAppSerializer