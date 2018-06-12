import time

import requests
import logging
from django.core.management import BaseCommand
from dapps.models import GitHub

logger = logging.getLogger('django')

spider_url = "https://spider.dapprank.com/schedule.json"


class Command(BaseCommand):
    def handle(self, *args, **options):
        for row in GitHub.objects.all():
            if row:
                logger.info(row.author_url)
                data = {
                    "project": "muon",
                    "spider": "github",
                    "url": row.author_url,
                }

                res = requests.post(
                    spider_url,
                    data=data,
                    auth=('spider', 'spider1@#')
                )
                if res.status_code == 200:
                    print(res.json())
                else:
                    logger.error(res.text)
                    # print(res.text)
                time.sleep(2)
