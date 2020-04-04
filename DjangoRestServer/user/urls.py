from rest_framework import status, generics
from rest_framework.response import Response


class AddRetrieveUserView(generics.ListCreateAPIView):

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)



class UpdateDeleteUserView(generics.RetrieveUpdateDestroyAPIView):

    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
    

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)