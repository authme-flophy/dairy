# Generated by Django 3.2.9 on 2021-11-18 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='customer_name',
            new_name='customer',
        ),
    ]
