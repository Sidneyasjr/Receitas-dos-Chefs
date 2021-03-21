from django.urls import path
from .views import recipe_view

urlpatterns = [
    path('receitas/', recipe_view.RecipeList.as_view(), name='recipe-list')
]