# Generated by Django 3.2 on 2022-05-27 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twofa', '0002_profile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
