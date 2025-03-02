# Generated by Django 5.1.5 on 2025-02-02 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_type', models.CharField(max_length=120)),
                ('issue_desc', models.CharField(max_length=300)),
                ('resoloved', models.BooleanField()),
                ('location_lat', models.FloatField()),
                ('location_long', models.FloatField()),
            ],
        ),
    ]
