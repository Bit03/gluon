import requests
from django.core.management import BaseCommand
from dapps.models import GitHub


class Command(BaseCommand):
    def handle(self, *args, **options):
        for row in GitHub.objects.all():
            print(row.author_url)
