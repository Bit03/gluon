from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.reverse import reverse


class DAppListAPIViewTestCase(APITestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_can_get_dapp_list_from_api(self):
        _url = reverse('api:dapps:list')
        res = self.client.get(_url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

