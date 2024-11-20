# Generated by Django 4.2.6 on 2024-11-20 06:38

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
            name='DepositProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dcls_month', models.TextField()),
                ('kor_co_nm', models.TextField()),
                ('fin_prdt_nm', models.TextField()),
                ('join_way', models.TextField()),
                ('mtrt_int', models.TextField()),
                ('spcl_cnd', models.TextField()),
                ('join_deny', models.IntegerField()),
                ('join_member', models.TextField()),
                ('etc_note', models.TextField()),
                ('max_limit', models.IntegerField()),
                ('fin_prdt_cd', models.TextField()),
                ('like_users', models.ManyToManyField(default=0, related_name='like_deposits', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DepositOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_prdt_cd', models.TextField()),
                ('intr_rate_type_nm', models.TextField()),
                ('save_trm', models.IntegerField()),
                ('intr_rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('intr_rate2', models.DecimalField(decimal_places=2, max_digits=10)),
                ('deposit_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deposit_options', to='deposits.depositproduct')),
            ],
        ),
    ]
