"""softdesk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_nested import routers
from api.views import ProjectViewSet, ContributorViewSet, IssueViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='projects')

contributor_router = routers.NestedDefaultRouter(router, r'projects', lookup='projects')
contributor_router.register(r'users', ContributorViewSet, basename='users')

issue_router = routers.NestedDefaultRouter(router, r'projects', lookup='projects')
issue_router.register(r'issues',IssueViewSet, basename='issues')

comment_router = routers.NestedDefaultRouter(issue_router, r'issues', lookup='issues')
comment_router.register(r'comments', CommentViewSet, basename='comments')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('', include(contributor_router.urls)),
    path('', include(issue_router.urls)),
    path('', include(comment_router.urls)),
]



