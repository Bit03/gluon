from applications.github.models import Repository
from django.core.management import BaseCommand
import requests
import logging


logger = logging.getLogger('django')


class Command(BaseCommand):

    def handle(self, *args, **options):
        for row in Repository.objects.all():
            logger.info(row.full_name)

            _url = "https://api.github.com/repos/{full_name}".format(
                full_name=row.full_name
            )
            res = requests.get(_url, timeout=5)
            if res.status_code == 200:
                data = res.json()
                logger.info(data)
                row.html_url = data['html_url']
                row.homepage = data['homepage']
                row.language = data['language']
                row.save()



