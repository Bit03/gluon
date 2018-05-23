from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from faker import Faker
from .faker_dapp import DappProvider
from dapps.models import DApp

fake = Faker()
fake.add_provider(DappProvider)


class DAppsViewTestCase(TestCase):
    def setUp(self):
        dapp = DApp()
        dapp.name = fake.name()
        dapp.platform = fake.word()
        dapp.license = fake.license()
        dapp.status = fake.status()
        dapp.save()

    def tearDown(self):
        DApp.objects.all().delete()

    def test_can_get_dapps_list(self):
        _url = reverse('dapps:list')
        res = self.client.get(_url)
        self.assertEqual(res.status_code, status.HTTP_302_FOUND)
