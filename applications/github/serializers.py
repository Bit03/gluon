from rest_framework import serializers
from applications.github.models import (
    People,
    Repository,
    RepositoryStats,
    Commit,
)


#
# class OrganizationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Organization
#         exclude = ("created_at", "id")
#         read_only_fields = ("slug",)


class PeopleSerializer(serializers.ModelSerializer):
    watch = serializers.IntegerField(default=0, source='get_watch', read_only=True)
    star = serializers.IntegerField(default=0, source='get_star', read_only=True)
    fork = serializers.IntegerField(default=0, source='get_fork', read_only=True)
    repos_count = serializers.IntegerField(default=0, source='get_repos_count', read_only=True)

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
        # read_only_fields = ('date',)
        # pandas_index = ['date']
        # pandas_unstacked_header = ['repos_id', ]

    def create(self, validated_data):
        return super().create(validated_data)


class RepositoryCommitSerializer(serializers.ModelSerializer):
    repos_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Commit
        fields = (
            "repos_id", "hash", "branch", "commit_datetime",
        )

