# Generated by Django 3.1.3 on 2020-12-24 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0005_home_page_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instagram', models.URLField()),
            ],
        ),
    ]
