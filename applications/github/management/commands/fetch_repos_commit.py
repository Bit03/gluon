from django.core.management import BaseCommand
from applications.github.models import Repository


class Command(BaseCommand):

    def handle(self, *args, **options):
        for row in Repository.objects.all():
            print(row.full_name, row.html_url, row.id)
