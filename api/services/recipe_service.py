from django.http import Http404

from ..models import Recipe


def list_recipes():
    recipes = Recipe.objects.all()
    return recipes


def register_recipe(recipe):
    recipe_bd = Recipe.objects.create(title=recipe.title, ingredients=recipe.ingredients, steps=recipe.steps,
                                      time=recipe.time, servings=recipe.servings, chef=recipe.chef, user=recipe.user)
    recipe_bd.save()
    return recipe_bd


def list_recipe_id(id):
    try:
        return Recipe.objects.get(id=id)
    except Recipe.DoesNotExist:
        raise Http404


def edit_recipe(old_recipe, new_recipe):
    old_recipe.title = new_recipe.title
    old_recipe.ingredients = new_recipe.ingredients
    old_recipe.steps = new_recipe.steps
    old_recipe.time = new_recipe.time
    old_recipe.servings = new_recipe.servings
    old_recipe.chef = new_recipe.chef
    old_recipe.save(force_update=True)


def remove_recipe(recipe):
    recipe.delete()