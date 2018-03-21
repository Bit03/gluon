import requests
import time
from dapps.models import GitHub
# from github.models import Author as github_authod


def run():
    g = GitHub.objects.all()

    for row in g:
        if row.author_url:
            payload = {
                "project": "default",
                "spider": "github",
                "url": row.author_url,
            }
            res = requests.post("http://spider.dapprank.com/schedule.json", data=payload)
            if res.status_code == 200:
                print (res.json())
        time.sleep(30)