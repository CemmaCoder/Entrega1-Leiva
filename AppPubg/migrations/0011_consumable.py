# Generated by Django 4.0.4 on 2022-06-08 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppPubg', '0010_equipament_capacity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consumable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('weight', models.IntegerField()),
                ('health', models.IntegerField()),
                ('boost', models.IntegerField()),
                ('image', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]