# Generated by Django 4.1 on 2022-08-20 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("heartdiseasepred", "0003_doctor"),
    ]

    operations = [
        migrations.AlterField(
            model_name="doctor",
            name="ConsultingHour",
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
