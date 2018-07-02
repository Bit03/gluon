from applications.github.models import Repository
from django.core.management import BaseCommand
import requests
import logging


logger = logging.getLogger('django')


class Command(BaseCommand):

    def handle(self, *args, **options):
        for row in Repository.objects.filter(state=True):
            logger.info(row.full_name)
            _url = "https://api.github.com/repos/{full_name}".format(
                full_name=row.full_name
            )
            headers = {
                "Authorization": "token 9284523b8916172be723b1dd4d8928a77273a731"
            }
            res = requests.get(_url, timeout=5, headers=headers)
            if res.status_code == 200:
                data = res.json()
                logger.info(data)
                row.html_url = data['html_url']
                row.homepage = data['homepage']
                row.language = data['language']
                row.created_at = data['created_at']
                row.updated_at = data['updated_at']
                row.pushed_at = data['pushed_at']
                row.stargazers_count = data['stargazers_count']
                row.watchers_count = data['watchers_count']
                row.forks_count = data['forks_count']
                row.save()
            elif res.status_code == 404:
                row.state = False
                row.save()
            else:
                logger.error(res.status_code)
                logger.error(res.content)



