# Generated by Django 3.0.5 on 2020-05-25 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CreateTask', '0003_auto_20200524_1308'),
    ]

    operations = [
        migrations.AddField(
            model_name='textdatainstance',
            name='IsViewing',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='textdatainstance',
            name='LastUpdate',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='textdatainstance',
            name='NumberOfAnnotations',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='textdatainstance',
            name='WhoIsViewing',
            field=models.IntegerField(default=0),
        ),
    ]
