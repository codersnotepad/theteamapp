# Generated by Django 3.2.13 on 2022-04-16 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resource', '0003_remove_fact_datetime_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='fact',
            name='employee_id',
            field=models.IntegerField(default=9999),
        ),
    ]
