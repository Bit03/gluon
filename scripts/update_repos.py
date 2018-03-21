import requests
import time
from github.models import Repository
spider_url = "http://spider.dapprank.com/schedule.json"


def run():
    for row in Repository.objects.all():
        print(row.id, row.url)
        data = {
            "project": "default",
            "spider": "repos",
            "repos_id": row.id,
            "url": row.url,
        }

        res = requests.post(spider_url, data=data)
        if res.status_code == 200:
            print (res.json())
        else:
            print (res.text)

        time.sleep(3)

