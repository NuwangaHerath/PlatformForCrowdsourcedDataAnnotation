# Generated by Django 3.0.6 on 2020-06-09 07:43

import CreateTask.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AnnotationTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False)),
                ('required_marks', models.IntegerField(default=50)),
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
                ('mediaData', models.FileField(upload_to=CreateTask.models.directory_path3)),
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
                ('status', models.CharField(default='inprogress', max_length=60)),
                ('instructions', models.CharField(max_length=1000)),
                ('field', models.CharField(default='', max_length=30)),
                ('taskType', models.CharField(max_length=10)),
                ('requiredNumofAnnotations', models.IntegerField(default=1)),
                ('creatorID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
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
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TestTextFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('csvFile', models.FileField(upload_to=CreateTask.models.directory_path5)),
                ('taskID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CreateTask.Task')),
            ],
        ),
        migrations.CreateModel(
            name='TestResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.DecimalField(decimal_places=2, max_digits=5)),
                ('annotatorID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('testID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CreateTask.AnnotationTest')),
            ],
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
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
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
            name='GenTextFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('csvFile', models.FileField(upload_to=CreateTask.models.directory_path)),
                ('taskID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CreateTask.Task')),
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
            name='DataGenTextInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(max_length=5000)),
                ('taskID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CreateTask.Task')),
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
