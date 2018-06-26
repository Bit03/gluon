from rest_framework import serializers
from applications.dapps.models import (
    DApp, Social, GitHub,
    Site, ContractAddress, EmailAddress
)


class SiteSerializers(serializers.ModelSerializer):
    logo_url = serializers.URLField()

    class Meta:
        model = Site
        exclude = ['id', 'logo', 'dapp']


class SocialSerializers(serializers.ModelSerializer):
    class Meta:
        model = Social
        exclude = ["id", "dapp"]


class GithubSerializers(serializers.ModelSerializer):
    watch = serializers.IntegerField(source='get_watch', default=0, read_only=True)
    star = serializers.IntegerField(source='get_star', default=0, read_only=True)
    fork = serializers.IntegerField(source='get_fork', default=0, read_only=True)
    repos_count = serializers.IntegerField(source='get_repos_count', default=0, read_only=True)

    class Meta:
        model = GitHub
        exclude = ["id", "dapp", "url"]


class EmailAddressSerializers(serializers.ModelSerializer):
    class Meta:
        model = EmailAddress
        exclude = ['id', 'dapp']


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
