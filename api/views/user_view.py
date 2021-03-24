from rest_framework import generics
from ..serializers import user_serializer



class UserList(generics.CreateAPIView):
    serializer_class = user_serializer.UserSerializer