# Generated by Django 3.2.3 on 2021-06-04 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='is_sold',
            field=models.BooleanField(default=False),
        ),
    ]
