from django.urls import path
from .views import ListRecipeView, DeleteRecipeView
urlpatterns = [
    path('task4/', ListRecipeView.as_view(), name="main"),
    path('delete/<int:pk>', DeleteRecipeView.as_view(), name='delete'),
]