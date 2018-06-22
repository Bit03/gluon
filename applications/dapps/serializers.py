from rest_framework import serializers
from applications.dapps.models import (
    DApp, Social, GitHub,
    Site, ContractAddress, EmailAddress
)


class SiteSerializers(serializers.ModelSerializer):
    logo_url = serializers.URLField()
    
    class Meta:
        model = Site
        exclude = ['id', 'logo']


class SocialSerializers(serializers.ModelSerializer):
    class Meta:
        model = Social
        exclude = ["id", "dapp"]


class GithubSerializers(serializers.ModelSerializer):
    class Meta:
        model = GitHub
        exclude = ["id", "dapp", "url"]


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
        exclude = ("id", "updated_at", "created_at", "is_removed",)


class DAppPlatformSerializers(serializers.Serializer):
    platform = serializers.CharField()

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
