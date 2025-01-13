from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView
from .models import OrderPosition

class ListRecipeView(ListView):
    model = OrderPosition
    context_object_name = 'orderpositions'
    template_name = 'Order_list.html'


class DeleteRecipeView(DeleteView):
    model = OrderPosition
    template_name = 'Order_delete.html'
    success_url = reverse_lazy('main')
