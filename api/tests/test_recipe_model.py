from django.test import TestCase
from api.models import Recipe


class RecipeModelTest(TestCase):
    def setUp(self):
        self.obj = Recipe(
            title='Miojo Cremoso',
            ingredients='1 pacote de macarrão instantâneo de qualquer sabor 4 colheres (sopa) de creme de leite 1 colher (sopa) de manteiga Cebola e tomate cortados em cubos a gosto',
            steps='Cozinhe o macarrão instantâneo normalmente.Em uma panela, coloque a manteiga, o tomate, a cebola e o tempero em pó do macarrão instantâneo para fritar, sempre mexendo bem para não empelotar.Depois despeje o creme de leite e misture o molho ao macarrão instantâneo',
            time='5 MIN',
            servings='1 PORÇÂO'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Recipe.objects.exists())


    def test_str(self):
        self.assertEqual('Miojo Cremoso', str(self.obj))