# Generated by Django 3.0.5 on 2020-05-24 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserManagement', '0004_auto_20200522_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='/static/img/avatar.png', null=True, upload_to='avatars/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(default='', max_length=255, null=True),
        ),
    ]
