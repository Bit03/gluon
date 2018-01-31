from rest_framework import serializers
from github.models import Author, AuthorProfile
# from dapps.models import DApp


# class DAppSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = DApp
#         exclude = ("updated_at", "created_at", "is_removed", )

class AuthorProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = AuthorProfile
        exclude = ("author", )


class AuthorSerializers(serializers.ModelSerializer):
    profile = AuthorProfileSerializers(read_only=True)

    class Meta:
        model = Author
        exclude = ("id", "created_at", "updated_at", )
