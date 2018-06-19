from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.reverse import reverse
from faker import Faker

from applications.dapps.models import DApp
from .faker_dapp import DappProvider

fake = Faker()
fake.add_provider(DappProvider)


class DAppListAPIViewTestCase(APITestCase):
    def setUp(self):
        self.dapp = DApp()
        self.dapp.name = fake.name()
        self.dapp.platform = fake.word()
        self.dapp.license = fake.license()
        self.dapp.status = fake.status()
        self.dapp.save()

    def tearDown(self):
        DApp.objects.all().delete()

    def test_can_get_dapp_list_from_api(self):
        _url = reverse('api:dapps:list')
        res = self.client.get(_url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        # print(res.json())
