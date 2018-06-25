import logging
from github import Github, UnknownObjectException
from applications.github.models import People

logger = logging.getLogger('django')


def run():
    g = Github("9284523b8916172be723b1dd4d8928a77273a731")
    users = People.objects.all()
    for row in users:
        print(row.login)
        try:
            user = g.get_user(row.login)
        except UnknownObjectException as e:
            print(row.login)
            logger.info(e)
            continue

        row.name = user.name
        row.avatar = user.avatar_url
        row.url = user.url
        row.html_url = user.html_url
        if user.type.lower() == 'user':
            row.type = People.TYPE.user
        else:
            row.type = People.TYPE.organization
        row.created_at = user.created_at
        row.updated_at = user.updated_at

        try:
            row.save()
        except Exception as e:
            print(row.url)
