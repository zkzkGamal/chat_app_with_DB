# Generated by Django 4.2.1 on 2023-05-06 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chat", "0002_rename_massage_job_order"),
    ]

    operations = [
        migrations.AlterField(
            model_name="job",
            name="name",
            field=models.TextField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name="job",
            name="order",
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
