# Generated by Django 4.0.6 on 2022-11-07 04:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='image',
        ),
    ]
