# Generated by Django 3.2.4 on 2021-07-20 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
