# Generated by Django 4.2.5 on 2023-09-24 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("us_nrc", "0008_alter_unit_report_reportdt"),
    ]

    operations = [
        migrations.AddField(
            model_name="reactor_unit",
            name="State",
            field=models.CharField(default="AK", max_length=100),
        ),
    ]
