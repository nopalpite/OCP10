# Generated by Django 4.1.7 on 2023-02-24 17:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.CharField(choices=[('read', 'read'), ('write', 'write')], default='read', max_length=50)),
                ('role', models.CharField(choices=[('author', 'author'), ('contributor', 'contributor')], default='contributor', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, max_length=8192)),
                ('type', models.CharField(choices=[('back-end', 'back-end'), ('front-end', 'front-end'), ('IOS', 'IOS'), ('android', 'android')], max_length=50)),
                ('user', models.ManyToManyField(through='api.Contributor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, max_length=8192)),
                ('tag', models.CharField(choices=[('bug', 'bug'), ('task', 'task'), ('improvement', 'improvement')], max_length=50)),
                ('priority', models.CharField(choices=[('low', 'low'), ('medium', 'medium'), ('high', 'high')], max_length=50)),
                ('status', models.CharField(choices=[('to do', 'to do'), ('in progress', 'in progress'), ('done', 'done')], max_length=50)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('assigned_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issue_assigned', to=settings.AUTH_USER_MODEL)),
                ('author_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issue_author', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.project')),
            ],
        ),
        migrations.AddField(
            model_name='contributor',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.project'),
        ),
        migrations.AddField(
            model_name='contributor',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, max_length=8192)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('author_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.issue')),
            ],
        ),
    ]
