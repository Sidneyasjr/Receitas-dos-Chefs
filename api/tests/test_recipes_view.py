import json

from django.test import TestCase
from django.urls import reverse, resolve
from rest_framework import status
from rest_framework.test import APIRequestFactory, APIClient

from ..models import Recipe, Chef
from ..views.recipe_view import RecipeList


class TestRecipeView(TestCase):
    def setUp(self):
        Chef.objects.create(name='Joao')
        self.chef = Chef.objects.get(name='Joao')
        Recipe.objects.create(title='Miojo', ingredients='Pacote', steps='Ferver', time='5 minutos',
                              servings='1 porção', chef=self.chef)
        self.recipe = Recipe.objects.get(title='Miojo')
        self.factory = APIRequestFactory()
        self.view = RecipeList.as_view()
        self.client = APIClient()
        self.data = {'title': 'Miojo', 'ingredients': 'Pacote', 'steps': 'Ferver', 'time': '5 minutos',
                     'servings': '1 porção', 'chef': 1}

    def test_recipe_view_success_status_code(self):
        url = reverse('recipe-list')
        request = self.factory.get(url)
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_recipes_url_resolves_view(self):
        view = resolve('/api/receitas/')
        self.assertEqual(view.func.view_class, RecipeList)

    def test_recipe_post_unauthorized_status_code(self):
        url = reverse('recipe-list')
        request = self.client.post(url, self.data)
        self.assertEqual(request.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_recipe_put_unauthorized_status_code(self):
        url = f'/api/receitas/{self.recipe.pk}/'
        request = self.client.put(url, self.data)
        self.assertEqual(request.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_recipe_delete_unauthorized_status_code(self):
        url = f'/api/receitas/{self.recipe.pk}/'
        request = self.client.delete(url)
        self.assertEqual(request.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_recipes_chefs_get_success_status_code(self):
        url = f'/api/chef/receitas/?chef={self.chef.pk}'
        request = self.factory.get(url)
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_search_recipes(self):
        url = f'/api/receitas/?search=miojo'
        request = self.factory.get(url)
        response = self.view(request)
        response.render()
        self.assertEqual(json.loads(response.content)[0]['id'], self.recipe.pk)
