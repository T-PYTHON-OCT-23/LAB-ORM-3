# Generated by Django 4.2.7 on 2023-12-06 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_review_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='user',
        ),
    ]
