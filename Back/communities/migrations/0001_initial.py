# Generated by Django 4.2.16 on 2024-11-26 16:46

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
            name='Community',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('keyword', models.CharField(choices=[('적금', 'saving'), ('예금', 'deposit'), ('지원금', 'subsidy'), ('기타', 'etc')], max_length=10)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='communities', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CommunityComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='communities.community')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='community_comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
