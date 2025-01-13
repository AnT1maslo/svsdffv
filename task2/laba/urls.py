from django.urls import path
from .views import ListRecipeView
urlpatterns = [
    path('recipe/', ListRecipeView.as_view(), name='recipe')
]