# Generated by Django 3.2.6 on 2021-10-25 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0019_auto_20211025_2348'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='telegram',
            field=models.URLField(blank=True, null=True),
        ),
    ]
