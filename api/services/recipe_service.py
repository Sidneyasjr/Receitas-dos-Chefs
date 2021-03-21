from ..models import Recipe


def list_recipes():
    recipes = Recipe.objects.all()
    return recipes


def register_recipe(recipe):
    recipe_bd = Recipe.objects.create(title=recipe.title, ingredients=recipe.ingredients, steps=recipe.steps,
                                      time=recipe.time, servings=recipe.servings)
    recipe_bd.save()
    return recipe_bd
