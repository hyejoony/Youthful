# Generated by Django 4.2.16 on 2024-11-19 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('savings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savingoption',
            name='saving_product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saving_options', to='savings.savingproduct'),
        ),
    ]
