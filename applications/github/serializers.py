import time
from rest_framework import serializers
from applications.github.models import (
    People,
    Repository,
    RepositoryStats,
    Commit,
)


class PeopleSerializer(serializers.ModelSerializer):
    watch = serializers.IntegerField(default=0, source='get_watch', read_only=True)
    star = serializers.IntegerField(default=0, source='get_star', read_only=True)
    fork = serializers.IntegerField(default=0, source='get_fork', read_only=True)
    repos_count = serializers.IntegerField(default=0, source='get_repos_count', read_only=True)

    class Meta:
        model = People
        exclude = ("id",)
        read_only_fields = ('created_at',)


class PeopleRankSerializer(serializers.Serializer):
    login = serializers.CharField()
    avatar = serializers.URLField()
    latest_7_day_commit = serializers.IntegerField(default=0)
    latest_30_day_commit = serializers.IntegerField(default=0)
    latest_90_day_commit = serializers.IntegerField(default=0)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


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

    def create(self, validated_data):
        return super().create(validated_data)


class RepositoryCommitSerializer(serializers.ModelSerializer):
    repos_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Commit
        fields = (
            "repos_id", "hash", "branch", "commit_datetime",
        )


class RepositoryCommitStateSerializer(serializers.Serializer):
    timestamp = serializers.SerializerMethodField()
    commit_count = serializers.IntegerField(default=0)

    def get_timestamp(self, obj):
        _date = obj['date']
        return time.mktime(_date.timetuple())

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class RepositoryStateChartSerializer(serializers.Serializer):
    timestamp = serializers.SerializerMethodField()
    watch = serializers.IntegerField(default=0)
    star = serializers.IntegerField(default=0)
    fork = serializers.IntegerField(default=0)

    def get_timestamp(self, obj):
        _date = obj.date
        return time.mktime(_date.timetuple())

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
