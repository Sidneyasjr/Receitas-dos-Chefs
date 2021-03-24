from rest_framework import filters
from rest_framework import generics
from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAuthenticated

from ..serializers import chef_serializer
from ..services import chef_service


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class ChefList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated | ReadOnly]
    queryset = chef_service.list_chefs()
    serializer_class = chef_serializer.ChefsSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class ChefDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated | ReadOnly]
    queryset = chef_service.list_chefs()
    serializer_class = chef_serializer.ChefsSerializer

