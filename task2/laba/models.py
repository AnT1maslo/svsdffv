from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=25)
    instructions = models.TextField(max_length=400)
    ingredient = models.ManyToManyField('Ingredient')

    def __str__(self):
        return f"{'/'.join(i.name for i in self.ingredient.all())}"


class Ingredient(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name
