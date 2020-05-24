# Generated by Django 3.0.5 on 2020-04-27 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CreateDataAnnotationTask', '0006_annotationdataset_who_is_viewing'),
    ]

    operations = [
        migrations.RenameField(
            model_name='annotationdataset',
            old_name='is_viewing',
            new_name='IsViewing',
        ),
        migrations.RenameField(
            model_name='annotationdataset',
            old_name='who_is_viewing',
            new_name='WhoIsViewing',
        ),
        migrations.AddField(
            model_name='annotationdataset',
            name='LastUpdate',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
