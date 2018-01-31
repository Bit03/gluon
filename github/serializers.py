from rest_framework import serializers
from github.models import Author
# from dapps.models import DApp


# class DAppSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = DApp
#         exclude = ("updated_at", "created_at", "is_removed", )


class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Author
        exclude = ("created_at", "updated_at", )
