# Generated by Django 4.2.9 on 2024-01-30 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='music',
            name='pub_date',
        ),
    ]
