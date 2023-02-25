from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from .models import Project, Contributor, Issue, Comment

class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ["id", "username"]

class ContributorSerializer(ModelSerializer):
    
    class Meta:
        model = Contributor
        fields = ["id", "user", "project", "permission", "role"]
        read_only_fields = ["project", "permission", "role"]

class ProjectSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = ["id", "title", "description", "type", "contributors"]

class IssueSerializer(ModelSerializer):

    class Meta:
        model = Issue
        fields = ["id", "project", "title", "description", "tag",
        "priority", "status", "author_user", "assigned_user", "created_time"]
        read_only_fields = ["project", "author_user", "created_time"]

class CommentSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = ["id", "issue", "description", "author_user", "created_time"]
        read_only_fields = ["issue", "author_user", "created_time"]


    