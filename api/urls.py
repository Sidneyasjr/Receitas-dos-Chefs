from django.urls import path
from .views import recipe_view, user_view

urlpatterns = [
    path('receitas/', recipe_view.RecipeList.as_view(), name='recipe-list'),
    path('receitas/<int:id>', recipe_view.RecipeDetails.as_view(), name='recipe-details'),
    path('usuario/', user_view.UserList.as_view(), name='user-list')
]