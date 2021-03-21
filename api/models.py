from django.db import models


class Recipe(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    ingredients = models.TextField(null=False, blank=False)
    steps = models.TextField(null=False, blank=False)
    time = models.CharField(max_length=20, null=False, blank=False)
    servings = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.title

