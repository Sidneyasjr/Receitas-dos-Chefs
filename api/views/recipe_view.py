from rest_framework import status
from rest_framework.permissions import IsAuthenticated, BasePermission, SAFE_METHODS
from rest_framework.response import Response
from rest_framework.views import APIView

from ..entities import recipe
from ..serializers import recipe_serializer
from ..services import recipe_service


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class RecipeList(APIView):
    permission_classes = [IsAuthenticated | ReadOnly]

    def get(self, request):
        recipes = recipe_service.list_recipes()
        serializer = recipe_serializer.RecipesSerializer(recipes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = recipe_serializer.RecipesSerializer(data=request.data)
        if serializer.is_valid():
            title = serializer.validated_data['title']
            ingredients = serializer.validated_data['ingredients']
            steps = serializer.validated_data['steps']
            time = serializer.validated_data['time']
            servings = serializer.validated_data['servings']
            chef = serializer.validated_data['chef']
            user = request.user
            new_recipe = recipe.Recipe(title=title, ingredients=ingredients, steps=steps, time=time, servings=servings,
                                       chef=chef, user=user)
            recipe_service.register_recipe(new_recipe)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RecipeDetails(APIView):
    permission_classes = [IsAuthenticated | ReadOnly]

    def get(self, request, id):
        recipe_id = recipe_service.list_recipe_id(id)
        serializer = recipe_serializer.RecipesSerializer(recipe_id)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        old_recipe = recipe_service.list_recipe_id(id)
        serializer = recipe_serializer.RecipesSerializer(old_recipe, data=request.data)
        if serializer.is_valid():
            title = serializer.validated_data['title']
            ingredients = serializer.validated_data['ingredients']
            steps = serializer.validated_data['steps']
            time = serializer.validated_data['time']
            servings = serializer.validated_data['servings']
            chef = serializer.validated_data['chef']
            user = old_recipe.user
            if old_recipe.user != request.user:
                return Response({"detail": 'Essa receita não pertence ao usuario logado'},
                                status=status.HTTP_403_FORBIDDEN)
            new_recipe = recipe.Recipe(title=title, ingredients=ingredients, steps=steps, time=time, servings=servings,
                                       chef=chef, user=user)
            recipe_service.edit_recipe(old_recipe, new_recipe)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        recipe_id = recipe_service.list_recipe_id(id)
        if recipe_id.user != request.user:
            return Response({"detail": 'Essa receita não pertence ao usuario logado'},
                            status=status.HTTP_403_FORBIDDEN)
        recipe_service.remove_recipe(recipe_id)
        return Response(status=status.HTTP_204_NO_CONTENT)
