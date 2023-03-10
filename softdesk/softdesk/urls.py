from django.contrib import admin
from django.urls import path, include
from rest_framework_nested import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api.views import ProjectViewSet, ContributorViewSet, IssueViewSet, CommentViewSet
from authentication.views import SignupView

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
    path('signup/', SignupView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('login/refresh/', TokenRefreshView.as_view()),
    path('', include(router.urls)),
    path('', include(contributor_router.urls)),
    path('', include(issue_router.urls)),
    path('', include(comment_router.urls)),
]



