# Generated by Django 3.2.6 on 2021-10-25 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0016_auto_20211025_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='link',
            field=models.ManyToManyField(blank=True, null=True, to='Home.contactLink'),
        ),
    ]
