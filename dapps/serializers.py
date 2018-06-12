from rest_framework import serializers
from dapps.models import DApp, Social


class SocialSerializers(serializers.ModelSerializer):
    class Meta:
        model = Social
        exclude = ["id", ]


class DAppSerializers(serializers.ModelSerializer):
    social = SocialSerializers()

    class Meta:
        model = DApp
        exclude = ("updated_at", "created_at", "is_removed",)
