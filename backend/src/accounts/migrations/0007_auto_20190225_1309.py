# Generated by Django 2.1.7 on 2019-02-25 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_orderpost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderpost',
            name='time',
            field=models.TimeField(blank=True),
        ),
    ]
