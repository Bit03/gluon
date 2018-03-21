# -*- coding: utf-8 -*-
import csv
from dapps.models import (DApp, EmailAddress, Social,
                          Site, ContractAddress, GitHub)


def process_tags(dapp, tags):
    _dapp = dapp
    _tags = tags
    for row in _tags:
        _dapp.tags.add(row.strip())


def process_email(dapp, email):
    _dapp = dapp
    _email = email
    email = EmailAddress()
    email.dapp = _dapp
    email.email = _email
    email.save()


def process_site(dapp, row):
    _dapp = dapp
    _row = row
    site = Site()
    site.dapp = _dapp
    site.url = _row["Site"]
    site.logo = _row["Logo"]
    site.whitepaper = _row["Whitepaper"]
    site.save()


def process_contract(dapp, row):
    _dapp = dapp
    _row = row
    contract = ContractAddress()
    contract.dapp = _dapp
    contract.mainnet = _row["Contract Address (mainnet)"]
    contract.ropsten = _row["Contract Address (ropsten)"]
    contract.kovan = _row["Contract Address (kovan)"]
    contract.rinkeby = _row["Contract Address (rinkeby)"]
    contract.save()


def process_github(dapp, row):
    _dapp = dapp
    _row = row
    github = GitHub()
    github.dapp = _dapp
    github.url = _row["GitHub"]
    github.save()


def process_social(dapp, row):
    _dapp = dapp
    _row = row
    social = Social()
    social.dapp = _dapp
    social.slack = _row["Slack"]
    social.gitter = _row["Gitter"]
    social.wiki = _row["Wiki"]
    social.facebook = _row["Facebook"]
    social.instagram = _row["Instagram"]
    social.twitter = _row["Twitter"]
    social.telegram = _row["Telegram"]
    social.youtube = _row["Youtube"]
    social.blog = _row["Blog"]
    social.medium = _row["Medium"]
    social.linkedin = _row["LinkedIn"]
    social.bitcointalk = _row["BitcoinTalk"]
    social.google_plus = _row["Google+"]
    social.kakao = _row["Kakao"]

    social.save()


def run():
    with open('scripts/dapps.csv', "r", encoding="utf-8", newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row['DAPP']
            # name = row.get('DAPP', None)
            #         if name:
            if len(name) == 0:
                continue
            # print (row["Submitted"])

            dapp = DApp()
            dapp.name = name.strip()
            dapp.platform = row["Platform"]
            dapp.symbol = row["Symbol"]
            dapp.description = row["Description"]
            dapp.description_cn = row["DescriptionCN"]
            dapp.country_of_origin = row['Country of origin']
            dapp.faq = row['FAQ']
            dapp.founder = row["Founder"]
            dapp.vc = row['VC']
            dapp.etherian = row["The Etherian"]

            dapp.license = row["License"]
            dapp.status = row["Status"]
            dapp.ico_status = row["ICOStatus"]

            if len(row["Submitted"]) > 0:
                dapp.submitted = row["Submitted"]
            if len(row["Last Update"]) > 0:
                dapp.last_update = row["Last Update"]
            dapp.save()

            if len(row["Contract Address (mainnet)"]) > 0 or \
                    len(row["Contract Address (ropsten)"]) > 0 or \
                    len(row["Contract Address (kovan)"]) > 0 or \
                    len(row["Contract Address (rinkeby)"]):
                process_contract(dapp, row)

            process_social(dapp, row)

            tag_string = row["Tags"]
            if len(tag_string) > 0:
                tags = tag_string.split(",")
                process_tags(dapp, tags)

            if len(row["Email"]) > 0:
                process_email(dapp, row["Email"])

            if len(row["Site"]) > 0:
                process_site(dapp, row)

            if len(row["GitHub"]) > 0:
                process_github(dapp, row)
