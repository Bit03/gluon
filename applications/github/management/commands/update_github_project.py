import logging
from time import sleep

from django.core.management import BaseCommand
from applications.github.models import People
from github import Github

logger = logging.getLogger('django')


class Command(BaseCommand):

    def handle(self, *args, **options):
        org = People.objects.filter(type=People.TYPE.organization)
        for row in org[:10]:
            logger.info(row.login)

            sleep(3)

