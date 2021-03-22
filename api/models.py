from django.contrib.auth.models import User
from django.db import models


class Recipe(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    ingredients = models.TextField(null=False, blank=False)
    steps = models.TextField(null=False, blank=False)
    time = models.CharField(max_length=20, null=False, blank=False)
    servings = models.CharField(max_length=50, null=False, blank=False)
    chef = models.CharField(max_length=30, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title

