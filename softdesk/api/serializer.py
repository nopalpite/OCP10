from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from models import Project, Contributor, Issue, Comment

class UserSerializer(ModelSerializer):

    class meta:
        model = User
        fields = ["id", "username"]

class ContributorSerializer(ModelSerializer):

    class meta:
        model = Contributor
        fields = ["id", "user", "project", "permission", "role"]

class ProjectSerializer(ModelSerializer):

    class meta:
        model = Project
        fields = ["id", "title", "description", "type", "user"]

class IssueSerializer(ModelSerializer):

    class meta:
        model = Issue
        fields = ["id", "project", "title", "description", "tag"
        "priority", "status", "author_user", "assigned_user", "created_time"]


class CommentSerializer(ModelSerializer):

    class meta:
        model = Comment
        fields = ["issue", "description", "author_user", "created_time"]

    