from rest_framework import serializers
from dapps.models import DApp, Social, GitHub, Site


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


class DAppSerializers(serializers.ModelSerializer):
    site = SiteSerializers()
    social = SocialSerializers()
    github = GithubSerializers()

    class Meta:
        model = DApp
        exclude = ("updated_at", "created_at", "is_removed",)
