# Generated by Django 4.1.7 on 2023-02-28 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pilotageApp', '0002_datapilotage_lumiere'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datapilotage',
            name='lumiere',
            field=models.FloatField(default=None, null=True),
        ),
    ]
