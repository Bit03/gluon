from rest_framework import serializers
from dapps.models import DApp, Social, GitHub


class SocialSerializers(serializers.ModelSerializer):
    class Meta:
        model = Social
        exclude = ["id", ]


class GithubSerializers(serializers.ModelSerializer):
    class Meta:
        model = GitHub
        exclude = ["id", ]


class DAppSerializers(serializers.ModelSerializer):
    social = SocialSerializers()
    github = GithubSerializers()

    class Meta:
        model = DApp
        exclude = ("updated_at", "created_at", "is_removed",)
