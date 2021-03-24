from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import generics
from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAuthenticated

from ..serializers import recipe_serializer
from ..services import recipe_service


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class RecipeList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated | ReadOnly]
    queryset = recipe_service.list_recipes()
    serializer_class = recipe_serializer.RecipesSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'ingredients', 'steps', 'time', 'servings']


class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated | ReadOnly]
    queryset = recipe_service.list_recipes()
    serializer_class = recipe_serializer.RecipesSerializer


class RecipeListChef(generics.ListAPIView):
    permission_classes = [IsAuthenticated | ReadOnly]
    queryset = recipe_service.list_recipes()
    serializer_class = recipe_serializer.RecipesSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['chef']

