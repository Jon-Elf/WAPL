# Generated by Django 3.2.4 on 2021-07-22 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_action_done'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='numb',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
