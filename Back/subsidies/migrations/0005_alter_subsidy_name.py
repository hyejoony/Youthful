# Generated by Django 4.2.16 on 2024-11-19 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subsidies', '0004_alter_subsidy_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subsidy',
            name='name',
            field=models.TextField(),
        ),
    ]