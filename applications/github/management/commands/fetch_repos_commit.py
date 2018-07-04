import logging
import requests
import time
from django.core.management import BaseCommand
from applications.github.models import Repository

logger = logging.getLogger('django')

spider_url = "https://spider.dapprank.com/schedule.json"


class Command(BaseCommand):

    def handle(self, *args, **options):
        for row in Repository.objects.filter(html_url__isnull=False):
            logger.info("{} - {} - {}".format(row.full_name, row.html_url, row.id))
            data = {
                "project": "muon",
                "spider": "commit",
                "repos_id": row.id,
                "url": row.html_url,
            }

            res = requests.post(spider_url, data=data, auth=('spider', 'spider1@#'))
            if res.status_code == 200:
                logger.info(res.json())
            else:
                logger.error(res.text)
            time.sleep(3)
