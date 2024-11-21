# Generated by Django 4.2.16 on 2024-11-21 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exchange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cur_unit', models.CharField(max_length=20)),
                ('link', models.TextField()),
                ('basic_rate', models.TextField()),
                ('remittance_send', models.TextField()),
                ('remittance_receive', models.TextField()),
                ('image_src', models.TextField()),
            ],
        ),
    ]
