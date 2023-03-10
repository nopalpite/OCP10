from django.db import models
from django.contrib.auth.models import User

TYPE = (
    ("back-end", "back-end"),
    ("front-end", "front-end"),
    ("IOS", "IOS"),
    ("android", "android")
)

PERMISSION = (
    ("read", "read"),
    ("write", "write")
)

ROLE = (
    ("author", "author"),
    ("contributor", "contributor")
)

TAG = (
    ("bug", "bug"),
    ("task", "task"),
    ("improvement", "improvement")
)

PRIORITY = (
    ("low", "low"),
    ("medium", "medium"),
    ("high", "high")
)

STATUS = (
    ("to do", "to do"),
    ("in progress", "in progress"),
    ("done", "done")
)


class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=8192, blank=True)
    type = models.CharField(max_length=50, choices=TYPE)
    contributors = models.ManyToManyField(User, through="Contributor")


class Contributor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    permission = models.CharField(
        max_length=50, choices=PERMISSION, default="read")
    role = models.CharField(max_length=50, choices=ROLE, default="contributor")

    class Meta:
        unique_together = ['user', 'project']


class Issue(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=8192, blank=True)
    tag = models.CharField(max_length=50, choices=TAG)
    priority = models.CharField(max_length=50, choices=PRIORITY)
    status = models.CharField(max_length=50, choices=STATUS)
    author_user = models.ForeignKey(
        User, related_name="issue_author", on_delete=models.CASCADE)
    assigned_user = models.ForeignKey(
        User, related_name="issue_assigned", on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    description = models.TextField(max_length=8192, blank=True)
    author_user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
