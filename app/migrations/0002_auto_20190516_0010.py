# Generated by Django 2.1.2 on 2019-05-16 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='access_token',
            field=models.CharField(max_length=2000, verbose_name='access token'),
        ),
        migrations.AlterField(
            model_name='token',
            name='refresh_token',
            field=models.CharField(max_length=200, verbose_name='refresh token'),
        ),
    ]