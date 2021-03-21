from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIRequestFactory

from ..models import Recipe
from ..views import recipe_view


class TestRecipeView(TestCase):
    def setUp(self):
        self.obj = Recipe.objects.create(
            title='Miojo',
            ingredients='1 pacote de macarrão instantâneo de qualquer sabor',
            steps='Cozinhe o macarrão instantâneo normalmente.',
            time='5 MIN',
            servings='1 PORÇÂO'
        )
        self.resp = reverse('recipe-details', kwargs={'id': self.obj.pk})
        self.factory = APIRequestFactory()
        self.view = recipe_view.RecipeDetails.as_view()
        self.data = dict(
            title='Miojo',
            ingredients='1 pacote de macarrão instantâneo de qualquer sabor',
            steps='Cozinhe o macarrão instantâneo normalmente.',
            time='5 MIN',
            servings='1 PORÇÂO'
        )

    def test_view_get_success_status_code(self):
        request = self.factory.get(self.resp)
        response = self.view(request, id=self.obj.pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_recipe_put_success_status_code(self):
        request = self.factory.put(self.resp, self.data)
        response = self.view(request, id=self.obj.pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_recipe_delete_success_status_code(self):
        request = self.client.delete(self.resp)
        self.assertEqual(request.status_code, status.HTTP_204_NO_CONTENT)
