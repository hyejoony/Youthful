# Generated by Django 4.2.16 on 2024-11-26 16:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('nickname', models.CharField(blank=True, max_length=100)),
                ('birthyear', models.IntegerField(validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(9999)])),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='profile/')),
                ('income', models.CharField(choices=[('0~50%', '약 100만원'), ('51~75%', '약 150만원'), ('76~100%', '약 200만원'), ('101~200%', '약 450만원'), ('200%~', '약 450초과')], max_length=20)),
                ('career', models.CharField(choices=[('학생', 'student'), ('회사원', 'office_worker'), ('사업자', 'business_owner'), ('아르바이트/비정규직', 'part_time'), ('무직/구직중', 'unemployed'), ('군인', 'soldier'), ('스타트업 창업자', 'startup_founder'), ('기타', 'other')], max_length=20)),
                ('region', models.CharField(choices=[('서울특별시', 'seoul'), ('부산광역시', 'busan'), ('대구광역시', 'daegu'), ('인천광역시', 'incheon'), ('광주광역시', 'gwangju'), ('대전광역시', 'daejeon'), ('울산광역시', 'ulsan'), ('세종특별자치시', 'sejong'), ('경기도', 'gyeonggi'), ('강원특별자치도', 'gangwon'), ('충청북도', 'chungbuk'), ('충청남도', 'chungnam'), ('전라북도', 'jeonbuk'), ('전라남도', 'jeonnam'), ('경상북도', 'gyeongbuk'), ('경상남도', 'gyeongnam'), ('제주특별자치도', 'jeju')], max_length=10)),
                ('condition1', models.BooleanField(default=False)),
                ('condition2', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
