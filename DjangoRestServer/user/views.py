from rest_framework import status, generics
from rest_framework.response import Response
from django.db import connection
from .serializer import MySerializer, AddUser, UpdateUser, RetrieveUsers


class AddRetrieveUserView(generics.GenericAPIView):

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            uid = serializer.validated_data['uid']
            name = serializer.validated_data['name']
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            with connection.cursor() as c:
                c.execute(
                    f"insert into test values('{uid}', '{name}', '{email}', '{password}')")
                return Response(status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request, *args, **kwargs):
        with connection.cursor() as c:
            c.execute('select * from test')
            users = c.fetchall()
            return Response({
                "users": users
            })

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddUser
        else:
            return RetrieveUsers


class UpdateDeleteUserView(generics.RetrieveUpdateDestroyAPIView):

    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return UpdateUser
