# Generated by Django 3.2 on 2021-05-01 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_advisor_advisor_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]