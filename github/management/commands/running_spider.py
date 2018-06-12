import requests
import time
import logging
from github.models import Repository
from django.core.management import BaseCommand


logger = logging.getLogger('django')

spider_url = "https://spider.dapprank.com/schedule.json"


class Command(BaseCommand):

    def handle(self, *args, **options):
        for row in Repository.objects.all():
            data = {
                "project": "muon",
                "spider": "repos",
                "repos_id": row.id,
                "url": row.url,
            }

            res = requests.post(spider_url, data=data, auth=('spider', 'spider1@#'))
            if res.status_code == 200:
                print(res.json())
            else:
                logger.error(res.text)
                # print(res.text)
            time.sleep(3)
