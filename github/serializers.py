from rest_framework import serializers
from github.models import (Organization, People,
                           Repository, RepositoryStats)


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        exclude = ("created_at", "id")
        read_only_fields = ("slug",)


class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        exclude = ("id",)
        read_only_fields = ('created_at',)


class RepositorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Repository
        exclude = ("id",)
        read_only_fields = ('created_at',)


class RepositoryStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepositoryStats
        fields = '__all__'
