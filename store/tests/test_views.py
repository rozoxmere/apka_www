from django.test import TestCase
from django.test import Client

from store.models import Osoba


class OsobaViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Osoba.objects.create(imie='Adam', nazwisko='Igielski', miesiac_urodzenia=1)


    def test_osoba_detail(self):
        c = Client()
        response = c.get('/store/persons/1')
        self.assertEqual(response.status_code, 200)