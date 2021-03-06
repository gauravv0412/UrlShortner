# Generated by Django 2.2.3 on 2019-07-30 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='database',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shortened_url', models.CharField(max_length=15)),
                ('actual_url', models.CharField(max_length=2048)),
                ('num_clicks', models.IntegerField(default=0)),
                ('tob', models.TimeField(auto_now=True)),
                ('dob', models.DateField(auto_now=True)),
            ],
        ),
    ]
