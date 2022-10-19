from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(blank=True, null=True, max_length=255)
    description = models.TextField(blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'product'

class Osoba(models.Model):
    MONTHS = (
        ("1", "Styczen"),
        ("2", "Luty"),
        ("3", "Marzec"),
        ("4", "Kwiecien"),
        ("5", "Maj"),
        ("6", "Czerwiec"),
        ("7", "Lipiec"),
        ("8", "Sierpien"),
        ("9", "Wrzesien"),
        ("10", "Pazdziernik"),
        ("11", "Listopad"),
        ("12", "Grudzien"),
    )
    imie = models.TextField(null=False, blank=False)
    nazwisko = models.TextField(null=False, blank=False)
    miesiac_urodzenia = models.CharField(max_length=2, choices=MONTHS, default=(MONTHS[0]))
    data_dodania = models.DateField(auto_now_add=True)