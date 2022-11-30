import datetime

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



class Druzyna(models.Model):
    nazwa = models.TextField();
    kraj = models.CharField(max_length=2)

    class Meta:
        verbose_name = "Drużyna"
        verbose_name_plural = "Drużyny"
    def __str__(self):
        return f"{self.nazwa} ({self.kraj})"

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
class Osoba(models.Model):
    imie = models.TextField(null=False, blank=False, verbose_name="Imię")
    nazwisko = models.TextField(null=False, blank=False)
    miesiac_urodzenia = models.IntegerField(choices=Months.choices)
    data_dodania = models.DateField(auto_now_add=True)
    druzyna = models.ForeignKey(Druzyna, on_delete=models.SET_NULL,  null=True)
    wlasciciel = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    def __str__(self):
        return f"{self.imie} {self.nazwisko}"

    class Meta:
        ordering = ["nazwisko"]

