# Generated by Django 4.0.4 on 2022-06-08 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppPubg', '0009_player_steam'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipament',
            name='capacity',
            field=models.IntegerField(null=True),
        ),
    ]