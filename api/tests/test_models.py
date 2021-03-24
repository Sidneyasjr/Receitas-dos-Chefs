from django.contrib.auth.models import User
from django.test import TestCase

from api.models import Recipe, Chef


class ModelsTest(TestCase):
    def setUp(self):
        self.chef = Chef.objects.create(name='Joao')
        self.chef_id = Chef.objects.get(name='Joao')
        self.recipe = Recipe.objects.create(title='Miojo', ingredients='Pacote', steps='Ferver', time='5 minutos',
                                            servings='1 porção', chef=self.chef_id)
        self.user = User.objects.create(username='Maria', password='123456')

    def test_create_chef(self):
        self.assertTrue(Chef.objects.exists())

    def test_str_chef(self):
        self.assertEqual('Joao', str(self.chef))

    def test_create_recipe(self):
        self.assertTrue(Recipe.objects.exists())

    def test_str_recipe(self):
        self.assertEqual('Miojo', str(self.recipe))

    def test_create_user(self):
        self.assertTrue(User.objects.exists())

    def test_str_user(self):
        self.assertEqual('Maria', str(self.user))
