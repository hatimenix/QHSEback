# Generated by Django 4.2 on 2023-04-12 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QHSEApi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='processus',
            name='processus_nom',
        ),
    ]
