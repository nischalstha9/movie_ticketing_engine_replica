# Generated by Django 3.1 on 2020-08-11 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Engine', '0002_auto_20200811_0719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seat',
            name='seat_no',
            field=models.PositiveIntegerField(unique=True),
        ),
    ]
