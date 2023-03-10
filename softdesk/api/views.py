from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import Project, Contributor, Issue
from .serializers import (
    ContributorSerializer,
    ProjectSerializer,
    IssueSerializer,
    CommentSerializer,
)
from .permissions import (
    IsProjectAuthorOrReadOnly,
    IsContributorAuthorOrReadOnly,
    IsAuthorOrReadOnly,
)


class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsProjectAuthorOrReadOnly]

    def get_queryset(self):
        return Project.objects.filter(contributors__id=self.request.user.id)

    def perform_create(self, serializer):
        project = serializer.save()
        Contributor.objects.create(
            user=self.request.user,
            project=project,
            permission="write",
            role="author",
        )


class ContributorViewSet(ModelViewSet):
    serializer_class = ContributorSerializer
    permission_classes = [IsAuthenticated, IsContributorAuthorOrReadOnly]

    def get_queryset(self):
        project = Project.objects.get(pk=self.kwargs['projects_pk'])
        return project.contributor_set.all()

    def perform_create(self, serializer):
        project = Project.objects.get(pk=self.kwargs['projects_pk'])
        serializer.save(project=project)


class IssueViewSet(ModelViewSet):
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def get_queryset(self):
        project = Project.objects.get(pk=self.kwargs['projects_pk'])
        return project.issue_set.all()

    def perform_create(self, serializer):
        project = Project.objects.get(pk=self.kwargs['projects_pk'])
        print(project)
        serializer.save(project=project, author_user=self.request.user)


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def get_queryset(self):
        issue = Issue.objects.get(pk=self.kwargs['issues_pk'])
        return issue.comment_set.all()

    def perform_create(self, serializer):
        issue = Issue.objects.get(pk=self.kwargs['issues_pk'])
        serializer.save(issue=issue, author_user=self.request.user)
