import csv
import logging
from applications.dapps.models import DApp, Site, Social

logger = logging.getLogger('django')


def process(dapp:DApp, row:dict):
    """

    :type dapp: object
    """
    logo_url = row['Logo']
    site_url = row['Site']
    whitepaper_url = row['Whitepaper']
    tags_string = row['Tags']

    if len(tags_string) > 0:
        tags = tags_string.split(',')
        for t in tags:
            dapp.tags.add(t.strip())
    if len(site_url) > 0:
        try:
            dapp.site.url = site_url
            dapp.site.logo = logo_url
            dapp.site.whitepaper = whitepaper_url
            dapp.site.save()
        except Exception as e:
            logger.info(e)
            s = Site()
            s.dapp = dapp
            s.logo = logo_url
            s.url = site_url
            s.whitepaper = whitepaper_url
            s.save()

    try:
        social = dapp.social
    except Exception:
        social = Social()
        social.dapp = dapp
    social.twitter = row['Twitter']
    social.facebook = row['Facebook']
    social.slack = row['Slack']
    social.telegram = row['Telegram']
    social.reddit = row['Reddit']
    social.instagram = row['Instagram']
    social.save()

def run():
    with open("scripts/dapps.csv", newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # print (row)

            try:
                dapp = DApp.objects.get(name=row['DAPP'])
                process(dapp=dapp, row=row)
            except DApp.DoesNotExist:
                dapp = DApp()
                dapp.name = row['DAPP']
                dapp.platform = row['Platform']
                dapp.symbol = row['Symbol']
                dapp.description = row['Description']
                dapp.description_cn = row['DescriptionCN']
                dapp.save()




            except DApp.MultipleObjectsReturned:
                print(row['DAPP'])
