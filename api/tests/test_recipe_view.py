from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIRequestFactory

from ..views import recipe_view


class TestRecipeView(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = recipe_view.RecipeList.as_view()
        self.data = {
            "title": "Titulo Test",
            "ingredients": "Teste",
            "steps": "Teste",
            "time": "5 MIN",
            "servings": "1 PORÇÂO"
        }

    def test_view_success_status_code(self):
        url = reverse('recipe-list')
        request = self.factory.get(url)
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_view_post_success_status_code(self):
        url = reverse('recipe-list')
        request = self.client.post(url, self.data)
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)
