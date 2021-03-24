from django.urls import path
from .views import recipe_view, user_view, chef_view

urlpatterns = [
    path('receitas/', recipe_view.RecipeList.as_view(), name='recipe-list'),
    path('chef/receitas/', recipe_view.RecipeListChef.as_view(), name='chef-recipes-list'),
    path('receitas/<int:pk>/', recipe_view.RecipeDetail.as_view(), name='recipe-detail'),
    path('chefs/', chef_view.ChefList.as_view(), name='chef-list'),
    path('chefs/<int:pk>/', chef_view.ChefDetail.as_view(), name='chef-detail'),
    path('usuario/', user_view.UserList.as_view(), name='user-list')
]