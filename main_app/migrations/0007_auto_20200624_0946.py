# Generated by Django 3.0.7 on 2020-06-24 16:46

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0006_comment_blog'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment',
            new_name='BlogComment',
        ),
    ]
