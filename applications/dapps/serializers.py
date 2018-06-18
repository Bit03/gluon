from rest_framework import serializers
from applications.dapps.models import (
    DApp, Social, GitHub,
    Site, ContractAddress, EmailAddress
)


class SiteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Site
        exclude = ['id']


class SocialSerializers(serializers.ModelSerializer):
    class Meta:
        model = Social
        exclude = ["id", ]


class GithubSerializers(serializers.ModelSerializer):
    class Meta:
        model = GitHub
        exclude = ["id", ]


class EmailAddressSerializers(serializers.ModelSerializer):
    class Meta:
        model = EmailAddress
        exclude = ['id', ]


class DAppSerializers(serializers.ModelSerializer):
    site = SiteSerializers()
    social = SocialSerializers()
    github = GithubSerializers()
    email = EmailAddressSerializers()

    class Meta:
        model = DApp
        exclude = ("updated_at", "created_at", "is_removed",)
