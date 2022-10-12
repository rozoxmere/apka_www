from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(blank=True, null=True, max_length=255)
    description = models.TextField(blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'product'
