# Generated by Django 4.0.4 on 2022-07-14 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]
