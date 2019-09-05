# Generated by Django 2.2 on 2019-08-30 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_models_from_csv', '0007_dynamicmodel_csv_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dynamicmodel',
            name='csv_google_refresh_token',
        ),
        migrations.AddField(
            model_name='dynamicmodel',
            name='csv_google_credentials',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dynamicmodel',
            name='csv_google_sheet_private',
            field=models.BooleanField(default=False),
        ),
    ]