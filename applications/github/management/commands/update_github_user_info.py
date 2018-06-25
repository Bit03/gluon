from django.core.management import BaseCommand
from applications.dapps.models import GitHub
from applications.github.models import People


class Command(BaseCommand):
    def handle(self, *args, **options):
        # for row in People.objects.all():
        #     print (row)

        for row in GitHub.objects.filter(state=True):
            # print (row.author)
            try:
                user = People.objects.get(login=row.author)
            except People.DoesNotExist:
                print(row.author, row)

                if row.author:
                    People.objects.create(
                        login=row.author
                    )
