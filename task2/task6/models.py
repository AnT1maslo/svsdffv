from django.db import models


class Recipe(models.Model):
    products = models.TextField(max_length=300)

    def __str__(self):
        return self.products


class Chef(models.Model):
    name = models.CharField(max_length=35)
    recipe = models.ForeignKey(Recipe, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
