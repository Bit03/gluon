import random
from faker import Faker
from faker.providers import BaseProvider

fake = Faker()


class DappProvider(BaseProvider):

    def status(self):
        stat = ["demo", "live", "concept", "wip"]
        return random.choice(stat)

    def license(self):
        licenses = ["MIT", "GPLv3", "Apache License 2.0", "proprietary", "GPL"]
        return random.choice(licenses)