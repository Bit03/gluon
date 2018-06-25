from applications.github.models import Organization, People


def run():
    repos = Organization.objects.all()

    for row in repos:
        # print(row.name, row.author)

        p = People()
        p.name = row.name
        p.login = row.author
        p.bio = row.bio
        p.location = row.location
        p.url = row.url
        p.html_url = row.url
        p.type = People.TYPE.organization
        p.save()
