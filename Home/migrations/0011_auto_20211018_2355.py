# Generated by Django 3.2.6 on 2021-10-18 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0010_auto_20211018_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='github',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='instagram',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='youtube',
            field=models.URLField(null=True),
        ),
    ]
