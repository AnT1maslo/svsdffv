from django.contrib import admin
from .models import OrderPosition, Order

admin.site.register(Order)
admin.site.register(OrderPosition)
