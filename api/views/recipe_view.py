from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ..services import recipe_service
from ..serializers import recipe_serializer
from ..entities import recipe


class RecipeList(APIView):
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
            new_recipe = recipe.Recipe(title=title, ingredients=ingredients, steps=steps, time=time, servings=servings)
            recipe_service.register_recipe(new_recipe)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
