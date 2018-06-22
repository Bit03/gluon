import logging
from django.core.management import BaseCommand
from applications.dapps.models import GitHub as dapp_github
from github import Github

logger = logging.getLogger('django')


class Command(BaseCommand):
    def handle(self, *args, **options):
        for row in dapp_github.objects.all():
            if row.author:
                logger.info(row.author)