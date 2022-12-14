# Generated by Django 4.1 on 2022-08-20 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("heartdiseasepred", "0002_datas_thal"),
    ]

    operations = [
        migrations.CreateModel(
            name="Doctor",
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
                ("Name", models.CharField(max_length=1000, null=True)),
                ("City", models.CharField(max_length=1000, null=True)),
                ("Qualification", models.CharField(max_length=1000, null=True)),
                ("Address", models.CharField(max_length=1000, null=True)),
                ("Phone", models.PositiveIntegerField(null=True)),
                ("Hotline", models.PositiveIntegerField(null=True)),
                ("ConsultingHour", models.TimeField(null=True)),
                ("ConsultingDay", models.CharField(max_length=1000, null=True)),
            ],
        ),
    ]
