# Generated by Django 3.0.5 on 2020-06-07 09:04

import CreateTask.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnnotationTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Cateogary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cateogaryName', models.CharField(max_length=250)),
                ('cateogaryTag', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ExampleMediaDataInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mediaData', models.FileField(upload_to=CreateTask.models.directory_path2)),
                ('testID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CreateTask.AnnotationTest')),
            ],
        ),
        migrations.CreateModel(
            name='ExampleTextDataInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CreateTask.AnnotationTest')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=1000)),
                ('status', models.CharField(default='new', max_length=60)),
                ('instructions', models.CharField(max_length=1000)),
                ('taskType', models.CharField(max_length=10)),
                ('requiredNumofAnnotations', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='UserNew2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='TextFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('csvFile', models.FileField(upload_to=CreateTask.models.directory_path)),
                ('taskID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CreateTask.Task')),
            ],
        ),
        migrations.CreateModel(
            name='TextDataInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NumberOfAnnotations', models.IntegerField(default=0)),
                ('IsViewing', models.BooleanField(default=False)),
                ('WhoIsViewing', models.IntegerField(default=0)),
                ('LastUpdate', models.DateTimeField()),
                ('taskID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CreateTask.Task')),
            ],
        ),
        migrations.CreateModel(
            name='TextData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Data', models.CharField(max_length=3000)),
                ('InstanceID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CreateTask.TextDataInstance')),
            ],
        ),
        migrations.CreateModel(
            name='TextAnnoAnswers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answerCateogary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CreateTask.Cateogary')),
                ('textInstance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CreateTask.ExampleTextDataInstance')),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CreateTask.UserNew2')),
            ],
        ),
        migrations.CreateModel(
            name='TestResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.DecimalField(decimal_places=2, max_digits=5)),
                ('annotatorID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CreateTask.UserNew2')),
                ('testID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CreateTask.AnnotationTest')),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='creatorID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CreateTask.UserNew2'),
        ),
        migrations.CreateModel(
            name='Questionaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='Active', max_length=20)),
                ('taskID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CreateTask.Task')),
            ],
        ),
        migrations.CreateModel(
            name='MediaDataInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media', models.FileField(upload_to=CreateTask.models.directory_path2)),
                ('NumberOfAnnotations', models.IntegerField(default=0)),
                ('IsViewing', models.BooleanField(default=False)),
                ('WhoIsViewing', models.IntegerField(default=0)),
                ('LastUpdate', models.DateTimeField()),
                ('taskID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CreateTask.Task')),
            ],
        ),
        migrations.CreateModel(
            name='MediaAnnoAnswers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answerCateogary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CreateTask.Cateogary')),
                ('mediaInstance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CreateTask.ExampleMediaDataInstance')),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CreateTask.UserNew2')),
            ],
        ),
        migrations.CreateModel(
            name='McqQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=2000)),
                ('questionaireID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CreateTask.Questionaire')),
            ],
        ),
        migrations.CreateModel(
            name='McqOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=1000)),
                ('is_correct', models.BooleanField(default=False)),
                ('questionID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CreateTask.McqQuestion')),
            ],
        ),
        migrations.CreateModel(
            name='ExampleTextData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Data', models.CharField(max_length=3000)),
                ('InstanceID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CreateTask.ExampleTextDataInstance')),
            ],
        ),
        migrations.CreateModel(
            name='ExampleTextAnnoResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ExampleTextDataInstanceID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CreateTask.ExampleTextDataInstance')),
                ('resultCateogary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CreateTask.Cateogary')),
            ],
        ),
        migrations.CreateModel(
            name='ExampleMediaAnnoResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ExampleMediaDataInstanceID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CreateTask.ExampleMediaDataInstance')),
                ('resultCateogary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CreateTask.Cateogary')),
            ],
        ),
        migrations.CreateModel(
            name='DescrptiveQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=2000)),
                ('questionaireID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CreateTask.Questionaire')),
            ],
        ),
        migrations.CreateModel(
            name='CateogaryTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TagNumber', models.IntegerField()),
                ('CateogaryID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CreateTask.Cateogary')),
            ],
        ),
        migrations.AddField(
            model_name='cateogary',
            name='taskID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CreateTask.Task'),
        ),
        migrations.AddField(
            model_name='annotationtest',
            name='taskID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CreateTask.Task'),
        ),
    ]
