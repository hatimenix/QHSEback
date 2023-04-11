# Generated by Django 4.1.7 on 2023-04-07 11:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("QHSEApi", "0005_remove_fichetechnique_url_fiche"),
    ]

    operations = [
        migrations.CreateModel(
            name="Secteurs",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("secteur_nom", models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name="fichetechnique",
            name="fichier",
            field=models.FileField(
                default=None,
                null=True,
                upload_to="uploads/",
                validators=[
                    django.core.validators.FileExtensionValidator(["pdf", "docx"])
                ],
            ),
        ),
        migrations.AlterField(
            model_name="utilisateur",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
    ]