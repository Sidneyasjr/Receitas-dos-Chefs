from rest_framework import serializers
from ..models import Recipe


class RecipesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('title', 'ingredients', 'steps', 'time', 'servings')