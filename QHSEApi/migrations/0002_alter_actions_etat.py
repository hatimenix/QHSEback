# Generated by Django 4.2 on 2023-04-27 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QHSEApi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actions',
            name='etat',
            field=models.CharField(blank=True, default='En cours', max_length=100),
        ),
    ]
