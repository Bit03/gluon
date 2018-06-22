from rest_framework import serializers
from applications.github.models import (
    Organization,
    People,
    Repository,
    RepositoryStats
)


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
    full_name = serializers.CharField(read_only=True)

    watch = serializers.IntegerField(default=0)
    star = serializers.IntegerField(default=0)
    fork = serializers.IntegerField(default=0)

    class Meta:
        model = Repository
        exclude = ('id', 'url',)
        read_only_fields = ('created_at',)


class RepositoryStatsSerializer(serializers.ModelSerializer):
    repos_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = RepositoryStats
        fields = ("repos_id", "watch", "star", "fork", "date")
        read_only_fields = ('date',)
        pandas_index = ['date']
        pandas_unstacked_header = ['repos_id', ]

    def create(self, validated_data):
        return super().create(validated_data)
