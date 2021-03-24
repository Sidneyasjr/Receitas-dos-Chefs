from django.test import TestCase
from django.urls import reverse, resolve
from rest_framework import status
from rest_framework.test import APIRequestFactory, APIClient

from ..models import Chef
from ..views.chef_view import ChefList


class TestChefView(TestCase):
    def setUp(self):
        Chef.objects.create(name='Joao')
        self.chef = Chef.objects.get(name='Joao')
        self.factory = APIRequestFactory()
        self.view = ChefList.as_view()
        self.client = APIClient()
        self.data = {'name': 'Joao'}

    def test_chef_view_success_status_code(self):
        url = reverse('chef-list')
        request = self.factory.get(url)
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_chefs_url_resolves_view(self):
        view = resolve('/api/chefs/')
        self.assertEqual(view.func.view_class, ChefList)

    def test_chef_post_unauthorized_status_code(self):
        url = reverse('chef-list')
        request = self.client.post(url, self.data)
        self.assertEqual(request.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_chef_put_unauthorized_status_code(self):
        url = f'/api/chefs/{self.chef.pk}/'
        request = self.client.put(url, self.data)
        self.assertEqual(request.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_chef_delete_unauthorized_status_code(self):
        url = f'/api/chefs/{self.chef.pk}/'
        request = self.client.delete(url)
        self.assertEqual(request.status_code, status.HTTP_401_UNAUTHORIZED)
