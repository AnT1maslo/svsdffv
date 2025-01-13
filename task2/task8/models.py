from django.db import models


class Device(models.Model):
    company = models.CharField(max_length=30)

    def __str__(self):
        return self.company


class SerialNumber(models.Model):
    number = models.PositiveIntegerField()
    device = models.OneToOneField(Device, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.number}, {self.device}"
