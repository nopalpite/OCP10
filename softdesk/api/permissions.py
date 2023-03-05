from rest_framework.permissions import BasePermission, SAFE_METHODS
from .models import Project

class IsProjectAuthorOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        contributor = obj.contributor_set.get(user=request.user)
        return contributor.permission == 'write'

class IsContributorAuthorOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        project = Project.objects.get(pk=view.kwargs.get('projects_pk'))
        contributor = project.contributor_set.get(user=request.user)
        return contributor.permission == 'write'

class IsAuthorOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        project = Project.objects.get(pk=view.kwargs.get('projects_pk'))
        contributor = project.contributor_set.get(user=request.user)
        return contributor.user == request.user
    
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author_user == request.user