from django.test import TestCase

from ..models import Osoba as Person, Druzyna


class PersonModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Person.objects.create(imie='Jan', nazwisko='Adamczyk', miesiac_urodzenia=5)

    def test_first_name_label(self):
        person = Person.objects.get(id=1)
        field_label = person._meta.get_field('imie').verbose_name
        self.assertEqual(field_label, 'Imię')

    def test_person_two_items_ids(self):
        Person.objects.create(imie='Adam', nazwisko='Igielski', miesiac_urodzenia=1)
        person1 = Person.objects.get(id=1)
        person2 = Person.objects.get(id=2)

class DruzynaModelTest(TestCase):
    def test_team_two_items_ids(self):
        Druzyna.objects.create(nazwa="Młoty Doroty", kraj="PL")
        Druzyna.objects.create(nazwa="Red Tigers", kraj="GB")
        team1 = Druzyna.objects.get(id=1)
        team2 = Druzyna.objects.get(id=2)

    def test_team_label(self):
        field_label = Druzyna._meta.verbose_name_plural
        self.assertEqual(field_label, 'Drużyny')