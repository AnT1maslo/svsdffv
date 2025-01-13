from django.db import models


class OrderPosition(models.Model):
    number = models.PositiveIntegerField()
    order = models.ForeignKey('Order', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.order}'


class Order(models.Model):
    title = models.CharField(max_length=25)
    price = models.FloatField()

    def __str__(self):
        return self.title
