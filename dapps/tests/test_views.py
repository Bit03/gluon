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
        self.dapp = DApp()
        self.dapp.name = fake.name()
        self.dapp.platform = fake.word()
        self.dapp.license = fake.license()
        self.dapp.status = fake.status()
        self.dapp.save()

    def tearDown(self):
        DApp.objects.all().delete()

    def test_can_search_dapps(self):
        _url = reverse('dapps:search')
        data = {
            'q': "eos"
        }
        res = self.client.get(_url, data=data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(res, 'dapps/list.html')

    def test_can_get_dapps_list(self):
        _url = reverse('dapps:list')
        res = self.client.get(_url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(res, 'dapps/list.html')

    def test_can_get_a_dapps(self):
        _url = reverse('dapps:detail', args=[self.dapp.slug])
        res = self.client.get(_url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(res, 'dapps/detail.html')

