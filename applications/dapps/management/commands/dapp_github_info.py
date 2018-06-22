import logging
from django.core.management import BaseCommand
from applications.dapps.models import GitHub as dapp_github

logger = logging.getLogger('django')


class Commands(BaseCommand):
    def handle(self, *args, **options):
        for row in dapp_github.objects.all():
            logger.info(row.author)