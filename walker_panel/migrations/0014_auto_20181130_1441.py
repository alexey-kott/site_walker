# Generated by Django 2.1.2 on 2018-11-30 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('walker_panel', '0013_auto_20181130_1349'),
    ]

    operations = [
        migrations.RenameField(
            model_name='log',
            old_name='date',
            new_name='datetime',
        ),
    ]