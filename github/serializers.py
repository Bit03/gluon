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

    date = serializers.SerializerMethodField(read_only=True)
    star = serializers.SerializerMethodField(read_only=True)
    fork = serializers.SerializerMethodField(read_only=True)
    watch = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Repository
        fields = ("identified_code", "author", "name", "desc",
                  "readme", "url", "date", "star", "fork", "watch")
        read_only_fields = ('created_at',)

    def get_star(self, obj):
        return obj.stats_df().star.diff().fillna(0).tolist()

    def get_fork(self, obj):
        return obj.stats_df().fork.diff().fillna(0).tolist()

    def get_watch(self, obj):
        return obj.stats_df().watch.diff().fillna(0).tolist()

    def get_date(self, obj):
        _date = map(lambda x: x.strftime("%Y-%m-%d"), obj.stats_df().index.tolist())
        return _date


class RepositoryStatsSerializer(serializers.ModelSerializer):
    repos_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = RepositoryStats
        fields = ("repos_id", "watch", "star", "fork", "date")
        read_only_fields = ('date',)

    def create(self, validated_data):
        return super().create(validated_data)
