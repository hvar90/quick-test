# Generated by Django 4.2.20 on 2025-04-01 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_rename_estimated_timee_delivery_estimated_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='estimated_time',
            field=models.DateTimeField(),
        ),
    ]
