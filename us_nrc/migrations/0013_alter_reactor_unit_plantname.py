# Generated by Django 4.2.5 on 2023-09-25 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("us_nrc", "0012_reactor_unit_id_alter_reactor_unit_plantname_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reactor_unit",
            name="PlantName",
            field=models.CharField(max_length=200),
        ),
    ]