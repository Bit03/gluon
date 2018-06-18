from django.test import TestCase
from dapps.models import DApp
from faker import Faker
from .faker_dapp import DappProvider


fake = Faker()
fake.add_provider(DappProvider)


class DappModelTestCase(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        DApp.objects.all().delete()

    def test_can_create_a_dapp(self):
        _count = DApp.objects.count()
        DApp.objects.create(
            name=fake.name(),
            platform=fake.word(),
            description=fake.text(),
        )
        _new = DApp.objects.count()
        self.assertGreater(_new, _count)
