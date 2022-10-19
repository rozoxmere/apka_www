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

    class Months(models.IntegerChoices):
        Styczen = 1
        Luty = 2
        Marzec = 3
        Kwiecien = 4
        Maj = 5
        Czerwiec = 6
        Lipiec = 7
        Sierpien = 8
        Wrzesien = 9
        Pazdziernik = 10
        Listopad = 11
        Grudzien = 12


    imie = models.TextField(null=False, blank=False)
    nazwisko = models.TextField(null=False, blank=False)
    miesiac_urodzenia = models.IntegerField(choices=Months.choices)
    data_dodania = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.imie} {self.nazwisko}"

    class Meta:
        ordering = ["nazwisko"]