# Generated by Django 3.1 on 2020-08-11 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Engine', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seat',
            name='seat_no',
            field=models.IntegerField(unique=True),
        ),
    ]