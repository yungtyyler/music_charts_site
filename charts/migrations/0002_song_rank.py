# Generated by Django 4.1.7 on 2023-02-21 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='rank',
            field=models.IntegerField(default=0),
        ),
    ]