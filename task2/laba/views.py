from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from .models import Recipe

class ListRecipeView(ListView):
    model = Recipe
    context_object_name = 'recipes'
    template_name = 'recipe_list.html'
