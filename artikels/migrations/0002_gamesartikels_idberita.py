# Generated by Django 4.1.3 on 2022-12-13 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("artikels", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="gamesartikels",
            name="idberita",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
