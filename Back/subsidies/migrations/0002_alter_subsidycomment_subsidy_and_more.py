# Generated by Django 4.2.16 on 2024-11-19 08:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subsidies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subsidycomment',
            name='subsidy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='subsidies.subsidy'),
        ),
        migrations.AlterField(
            model_name='subsidycomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subsidy_comments', to=settings.AUTH_USER_MODEL),
        ),
    ]