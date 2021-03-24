from ..models import Recipe


def list_recipes():
    recipes = Recipe.objects.all()
    return recipes
