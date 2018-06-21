import logging
from github import Github, UnknownObjectException
from applications.github.models import People

logger = logging.getLogger('django')


def run():
    g = Github("9284523b8916172be723b1dd4d8928a77273a731")
    users = People.objects.all()
    for row in users:
        print(row.nickname)
        try:
            user = g.get_user(row.nickname)
        except UnknownObjectException as e:
            print (row.nickname)
            logger.info(e)
            continue

        row.name = user.name
        # row.bio = user.bio
        row.url = user.url
        row.html_url = user.html_url
        if user.type.lower() == 'user':
            row.type = People.TYPE.user
        else:
            row.type = People.TYPE.organization
        row.created_at = user.created_at
        row.updated_at = user.updated_at

        row.save()
