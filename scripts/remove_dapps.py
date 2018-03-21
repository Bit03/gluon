from dapps.models import (DApp, EmailAddress, Site,
                          ContractAddress, GitHub, Social)


def run():
    Social.objects.all().delete()
    GitHub.objects.all().delete()
    ContractAddress.objects.all().delete()
    Site.objects.all().delete()
    EmailAddress.objects.all().delete()
    DApp.objects.all().delete()