# Generated by Django 2.1.2 on 2018-12-03 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('walker_panel', '0017_auto_20181202_2110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proxy',
            name='proxy_id',
        ),
        migrations.AddField(
            model_name='proxy',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
