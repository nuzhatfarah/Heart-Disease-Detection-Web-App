# Generated by Django 4.1 on 2022-08-20 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Datas",
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
                ("age", models.PositiveIntegerField(null=True)),
                ("sex", models.PositiveIntegerField(null=True)),
                ("cp", models.PositiveIntegerField(null=True)),
                ("trestbps", models.PositiveIntegerField(null=True)),
                ("chol", models.PositiveIntegerField(null=True)),
                ("fbs", models.PositiveIntegerField(null=True)),
                ("restecg", models.PositiveIntegerField(null=True)),
                ("thalach", models.PositiveIntegerField(null=True)),
                ("exang", models.PositiveIntegerField(null=True)),
                ("oldpeak", models.FloatField(null=True)),
                ("slope", models.PositiveIntegerField(null=True)),
                ("ca", models.PositiveIntegerField(null=True)),
                ("target", models.PositiveIntegerField(null=True)),
            ],
        ),
    ]
