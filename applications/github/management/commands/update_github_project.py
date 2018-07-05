import logging
from time import sleep

from django.core.management import BaseCommand
from applications.github.models import People, Repository
from github import Github, UnknownObjectException

logger = logging.getLogger('django')


class Command(BaseCommand):
    g = Github("9284523b8916172be723b1dd4d8928a77273a731")

    def handle(self, *args, **options):
        org = People.objects.filter(type=People.TYPE.organization, alive=True)
        for row in org[:10]:
            logger.info(row.login)

            try:
                user = self.g.get_user(row.login)
            except UnknownObjectException:
                row.alive = False
                row.save()
                logger.info("{} dead".format(row.login))
                continue

            for repo in user.get_repos():
                print(repo.name, repo.full_name, repo.html_url)

                try:
                    Repository.objects.get(author=row.login, name=repo.name)
                except Repository.DoesNotExist:
                    Repository.objects.create(
                        author=row.login,
                        name=repo.name,
                        url=repo.url,
                        html_url=repo.html_url,
                    )

            sleep(3)
