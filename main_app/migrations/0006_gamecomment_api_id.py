# Generated by Django 3.0.7 on 2020-06-25 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20200625_1109'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamecomment',
            name='api_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]