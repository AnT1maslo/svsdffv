from django.contrib import admin
from .models import Device, SerialNumber

admin.site.register(Device)
admin.site.register(SerialNumber)
