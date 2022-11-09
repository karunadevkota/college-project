# Generated by Django 4.0.6 on 2022-11-07 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_record_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChartData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('robbery', models.IntegerField()),
                ('domestic_violence', models.IntegerField()),
                ('sexual_harrasement', models.IntegerField()),
                ('missing', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='news',
            name='image',
        ),
        migrations.AlterField(
            model_name='record',
            name='description',
            field=models.TextField(max_length=500),
        ),
    ]
