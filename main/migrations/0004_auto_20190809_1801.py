# Generated by Django 2.2.3 on 2019-08-09 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20190807_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='database',
            name='actual_url',
            field=models.URLField(max_length=2048),
        ),
    ]
