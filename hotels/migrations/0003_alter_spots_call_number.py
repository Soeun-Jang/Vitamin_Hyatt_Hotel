# Generated by Django 4.2.1 on 2023-05-12 02:27

from django.db import migrations, models
import hotels.validators


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0002_alter_spots_call_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spots',
            name='call_number',
            field=models.CharField(max_length=20, unique=True, validators=[hotels.validators.validate_phone_number]),
        ),
    ]