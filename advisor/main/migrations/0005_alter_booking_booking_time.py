# Generated by Django 3.2 on 2021-05-01 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_booking_booking_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_time',
            field=models.DateTimeField(),
        ),
    ]