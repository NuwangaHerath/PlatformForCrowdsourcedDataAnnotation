# Generated by Django 3.0.5 on 2020-06-07 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnnotationDataSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NumberOfAnnotations', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200)),
                ('Description', models.TextField(blank=True, max_length=256)),
                ('DataInstanceAnnotationTimes', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='DataClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ClassName', models.CharField(max_length=100)),
                ('ClassID', models.IntegerField(default=0)),
                ('TaskID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ImageDataAnalyse.Task')),
            ],
        ),
        migrations.CreateModel(
            name='AnnotationDataSetresult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ClassID', models.IntegerField(default=0)),
                ('UserID', models.IntegerField()),
                ('LastUpdate', models.DateTimeField(auto_now=True)),
                ('Datainstance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ImageDataAnalyse.AnnotationDataSet')),
                ('TaskID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ImageDataAnalyse.Task')),
            ],
        ),
        migrations.AddField(
            model_name='annotationdataset',
            name='TaskID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ImageDataAnalyse.Task'),
        ),
    ]
