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
    repos_id = serializers.IntegerField(write_only=True)
    

    class Meta:
        model = RepositoryStats
        fields = ("repos_id", "watch", "star", "fork", "date")
        read_only_fields = ('date',)

    def create(self, validated_data):
        # print(validated_data)
        return super().create(validated_data)
