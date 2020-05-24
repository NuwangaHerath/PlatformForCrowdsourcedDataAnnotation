# Generated by Django 3.0.5 on 2020-05-19 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CreateDataGenerationTask', '0003_auto_20200425_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generationdataset',
            name='DataInstance',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='Description',
            field=models.TextField(blank=True, max_length=255),
        ),
    ]
