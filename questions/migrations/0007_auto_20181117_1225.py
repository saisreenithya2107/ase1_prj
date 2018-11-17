# Generated by Django 2.1.2 on 2018-11-17 06:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0006_auto_20181117_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='attempt_number',
            field=models.IntegerField(default=0, editable=False, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
