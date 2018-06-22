import logging
from django.core.management import BaseCommand
from applications.dapps.models import GitHub as dapp_github
from github import Github, UnknownObjectException

logger = logging.getLogger('django')


class Command(BaseCommand):
    def handle(self, *args, **options):
        for row in dapp_github.objects.all():
            if row.author:
                logger.info(row.author)
                g = Github("9284523b8916172be723b1dd4d8928a77273a731")
                try:
                    user = g.get_user(row.author)
                except UnknownObjectException:
                    continue

                row.login = user.login
                row.avatar_url = user.avatar_url
                row.url = user.url
                row.html_url = user.html_url
                row.save()