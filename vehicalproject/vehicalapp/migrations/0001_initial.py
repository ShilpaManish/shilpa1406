# Generated by Django 4.1.2 on 2022-12-19 12:16

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
            name='MechanicProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobnumber', models.IntegerField()),
                ('dob', models.DateField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('state', models.CharField(blank=True, max_length=30, null=True)),
                ('city', models.CharField(blank=True, max_length=30, null=True)),
                ('profpic', models.ImageField(default='', upload_to='images')),
                ('vehicalno', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobnumber', models.IntegerField()),
                ('dob', models.DateField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('state', models.CharField(blank=True, max_length=30, null=True)),
                ('city', models.CharField(blank=True, max_length=30, null=True)),
                ('profpic', models.ImageField(default='', upload_to='images')),
                ('vehicalno', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
