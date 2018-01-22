from rest_framework import serializers
from dapps.models import DApp


class DAppSerializers(serializers.ModelSerializer):
    class Meta:
        model = DApp
        exclude = ("updated_at", "created_at", "is_removed", )
