from applications.github.models import Organization


def run():
    repos = Organization.objects.all()

    for row in repos:
        print(row.name, row.author)
