from rest_framework import generics
from github.serializers import AuthorSerializers
from github.models import Author


class AuthorListAPIView(generics.ListCreateAPIView):
    serializer_class = AuthorSerializers
    queryset = Author.objects.all()