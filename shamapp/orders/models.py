from django.db import models

# Create your models here.

class Provider(models.Model):
    full_name = models.CharField(max_length=100)
    url = models.URLField()
    opening_hour = models.TimeField()
    closing_hour = models.TimeField()
    delivery_cost = models.DecimalField(
        decimal_places=2,
        max_digits=5,
    )
    minimal_order_amount = models.DecimalField(
        decimal_places=2,
        max_digits=5,
    )
