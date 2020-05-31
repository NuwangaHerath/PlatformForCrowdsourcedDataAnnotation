from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic.edit import CreateView, FormView
from django.views.generic import View
from .forms import CreateTaskForm, CateogaryFormSet, DQuestionFormSet, McqFormSet, McqForm, CustomForm1, CsvForm
from .models import UserNew2, Cateogary, DescrptiveQuestion, McqQuestion, McqOption, Questionaire, TextFile, \
    TextDataInstance, TextData, MediaDataInstance, Task, GenTextFile, DataGenTextInstance,TestTextFile,\
    ExampleTextDataInstance,ExampleTextData,ExampleTextAnnoResult,AnnotationTest
from django.forms import formset_factory
from django import template
from random import shuffle
from django.core.files.base import ContentFile
from django.conf import settings
from zipfile import ZipFile
import sys
import os
from PIL import Image
import csv


def test(request, task):
    print(task)
    return render(request, 'createtask/success.html')


def createTask(request):
    template_name = 'createtask/new.html'
    if request.method == 'GET':
        taskform = CreateTaskForm(request.GET or None)
        formset = CateogaryFormSet(queryset=Cateogary.objects.none())
        # print(taskform.name.label)

    elif request.method == 'POST':
        taskform = CreateTaskForm(request.POST)
        formset = CateogaryFormSet(request.POST)
        if taskform.is_valid() and formset.is_valid():
            task = taskform.save(commit=False)
            task.creatorID = UserNew2.objects.get(name='kasun')
            task.taskType = "ImageAnno"
            numAnnos = request.POST['NumAnnotations']
            # print(numAnnos)
            task.requiredNumofAnnotations = numAnnos
            task.save()
            request.session['task'] = task.id
            tag = 0
            for form in formset:
                # so that `book` instance can be attached.
                cateogary = form.save(commit=False)
                cateogary.taskID = task
                cateogary.cateogaryTag = tag
                cateogary.save()
                tag += 1
            # return render(request, 'createtask/success.html')
            files = request.FILES.getlist('file_field')
            print(files)
            processImages(files, task)
            return redirect('createtask:question_add')

    return render(request, template_name, {
        'taskform': taskform,
        'formset': formset,
    })


def processImages(files, task):
    images = []
    for image in files:
        if image.content_type[:5] == 'image':
            imgObj = MediaDataInstance(taskID=task, media=image)
            images.append(imgObj)
        else:
            pass
    MediaDataInstance.objects.bulk_create(images)


def createTextTask(request):
    template_name = 'createtask/addtextAnno.html'
    if request.method == 'GET':
        taskform = CreateTaskForm(request.GET or None)
        formset = CateogaryFormSet(queryset=Cateogary.objects.none())
        csvform = CsvForm()
        # print(taskform.name.label)

    elif request.method == 'POST':
        taskform = CreateTaskForm(request.POST)
        formset = CateogaryFormSet(request.POST)
        csvform = CsvForm(request.POST, request.FILES)
        if taskform.is_valid() and formset.is_valid() and csvform.is_valid():
            task = taskform.save(commit=False)
            task.creatorID = UserNew2.objects.get(name='kasun')
            csvFile = request.FILES['data']
            newFileModel = TextFile()
            task.taskType = "TextAnno"
            task.save()
            newFileModel.taskID = task
            newFileModel.csvFile = csvFile
            newFileModel.save()
            # print(newFileModel.csvFile.path)
            print(newFileModel.csvFile.url)
            filename = './' + newFileModel.csvFile.url
            words =ProcessCsv(filename, task)
            print('words='+str(words))
            request.session['task'] = task.id
            request.session['words'] = words   # for validating example adding csv
            tag = 0
            for form in formset:
                # so that `book` instance can be attached.
                cateogary = form.save(commit=False)
                cateogary.taskID = task
                cateogary.cateogaryTag = tag
                cateogary.save()
                tag += 1
            # return render(request, 'createtask/success.html')
            return redirect('createtask:TextAnno_example_add')

    return render(request, template_name, {
        'taskform': taskform,
        'formset': formset,
        'csvform': csvform,
    })


def ProcessCsv(filename, task):
    words = 0
    with open(filename, "r") as f:
        reader = csv.reader(f, delimiter=",")
        instancelist = []
        datalist = []
        for i, line in enumerate(reader):
            if i == 0:
                continue
            else:
                datainstance = TextDataInstance(taskID=task)
                instancelist.append(datainstance)
        TextDataInstance.objects.bulk_create(instancelist)
        real_objects = TextDataInstance.objects.filter(taskID=task)
        print('Helllloooo')
        #print(real_objects)
    with open(filename, "r") as f:
        reader = csv.reader(f, delimiter=",")
        for i, line in enumerate(reader):
            # print(instancelist[i-1])
            if i == 0:
                words = len(line)
                continue
            else:
                for word in line:
                    data = TextData(Data=word, InstanceID=real_objects[i - 1])
                    datalist.append(data)

        TextData.objects.bulk_create(datalist)
    return words


def AddTextAnnoExamples(request):
    template_name = 'createtask/addTextAnnoExamples.html'
    csvform = CsvForm()
    task = Task.objects.get(id=request.session['task'])
    words = request.session['words']
    cateogary_list = task.cateogary_set.all()
    if request.method == 'GET':
        context = {'cateogary_list': cateogary_list,'csvform':csvform}
        return render(request, template_name, context)
        # get task,get cateogaries print them in template form

    if request.method == 'POST':
        dic={}
        for cateogary in cateogary_list:
            name = str(cateogary.id)
            #print(name)
            tag = request.POST[name]                #handle errors
            dic.update({tag:cateogary})
        print(dic)
        
        csvFile = request.FILES['data']                #handle errors
        examplefile = TestTextFile(taskID=task, csvFile=csvFile)
        examplefile.save()
        filename = './' + examplefile.csvFile.url
        test = AnnotationTest(taskID = task)               #check checkbox
        isTest = request.POST['checktest']             #handle errors
        if isTest == 'checked':
            isTest = True
        else:
            isTest =False             
        print('isTest='+str(isTest))
        test.is_active = isTest
        test.save()
        processExampleCsvFile(filename,task,words,test,dic)
        return render(request, 'createtask/success.html')

def processExampleCsvFile(filename,task,words,test,dic):
    wrong_format = False
    with open(filename, "r") as f:
        reader = csv.reader(f, delimiter=",")
        exampleinstancelist = []
        exampledatalist = []
        exampleAnnotationresult = []
        for i, line in enumerate(reader):
            if i == 0:
                continue
            elif i == 21 :
                break
            else:
                exampledatainstance = ExampleTextDataInstance(testID=test)
                exampleinstancelist.append(exampledatainstance)
        ExampleTextDataInstance.objects.bulk_create(exampleinstancelist)
        real_objects = ExampleTextDataInstance.objects.filter(testID=test)

        #print(real_objects)
    with open(filename, "r") as f:
        reader = csv.reader(f, delimiter=",")
        for i, line in enumerate(reader):
            # print(instancelist[i-1])
            if i == 0:
                continue
            elif i == 21:
                break
            else:
                for j in range(words):
                    data = ExampleTextData(Data=line[j], InstanceID=real_objects[i - 1])
                    exampledatalist.append(data)
                result = str(line[words])
                print('result='+str(result))
                resultCateogary = dic[result]
                resultobject = ExampleTextAnnoResult(ExampleTextDataInstanceID=real_objects[i - 1],resultCateogary=resultCateogary)
                exampleAnnotationresult.append(resultobject)


        ExampleTextData.objects.bulk_create(exampledatalist)
        ExampleTextAnnoResult.objects.bulk_create(exampleAnnotationresult)



def AddQuestions(request):
    template_name = 'createtask/addQuestions.html'

    if request.method == 'GET':
        Dq_formset = DQuestionFormSet(queryset=DescrptiveQuestion.objects.none())
        Mcq_formset = McqFormSet()

    elif request.method == 'POST':
        Dq_formset = DQuestionFormSet(request.POST)
        Mcq_formset = McqFormSet(request.POST)
        if Dq_formset.is_valid() and Mcq_formset.is_valid():
            questionaire = Questionaire()
            task = Task.objects.get(id=request.session['task'])
            questionaire.taskID = task
            questionaire.save()
            for form in Dq_formset:
                Dquestion = form.save(commit=False)
                Dquestion.questionaireID = questionaire
                Dquestion.save()

            for form in Mcq_formset:
                # rough = McqForm(request.POST)
                rough1 = form.cleaned_data
                description = rough1.get('description')
                answer = rough1.get('correctanswer')
                option1 = rough1.get('option1')
                option2 = rough1.get('option2')
                option3 = rough1.get('option3')
                option4 = rough1.get('option4')
                mcq = McqQuestion()
                mcq.description = description
                mcq.questionaireID = questionaire
                mcq.save()
                answer1 = McqOption()
                answer1.is_correct = True
                answer1.description = answer
                answer1.questionID = mcq
                answer1.save()
                for i in range(4):
                    option = McqOption()
                    option.description = rough1.get('option' + str(i + 1))
                    option.questionID = mcq
                    option.save()

            return render(request, 'createtask/success.html')

    return render(request, template_name, {
        'Dq_formset': Dq_formset,
        'Mcq_formset': Mcq_formset,
    })


class TaskView(generic.ListView):
    template_name = 'createtask/Tasklits.html'
    context_object_name = 'all_tasks'

    def get_queryset(self):
        return Task.objects.all()


def QuestionaireView(request, task_id):
    # template_name = 'viewQuestions.html'

    if request.method == 'GET':
        task = Task.objects.get(pk=task_id)
        questionaire = Questionaire.objects.get(taskID=task)  # try required
        question_list = questionaire.mcqquestion_set.all()
        answers = []
        for i in question_list:
            a = i.mcqoption_set.all()
            answers.append(a)
            l = list(a)
            shuffle(l)
            i.add = l
        lenght = len(question_list)
        context = {'question_list': question_list, 'answers': answers, 'lenght': lenght}
        return render(request, 'createtask/viewQuestions.html', context)


def createGenerationTask(request):
    template_name = 'createtask/genarationtask_form.html'
    if request.method == 'GET':
        customform = CustomForm1()
        taskform = CreateTaskForm(request.GET or None)
        formset = CateogaryFormSet(queryset=Cateogary.objects.none())

        # print(taskform.name.label)

    elif request.method == 'POST':
        taskform = CreateTaskForm(request.POST)
        formset = CateogaryFormSet(request.POST)
        customform = CustomForm1(request.POST)
        if taskform.is_valid() and formset.is_valid() and customform.is_valid():
            task = taskform.save(commit=False)
            task.creatorID = UserNew2.objects.get(name='kasun')
            rough = customform.cleaned_data
            dataType = rough.get('dataType')
            if dataType == 'T':
                task.taskType = "TextGen"
            elif dataType == 'I':
                task.taskType = "ImageGen"
            task.save()
            request.session['task'] = task.id  # task id session created
            tag = 0
            for form in formset:
                # so that `book` instance can be attached.
                generationClass = form.save(commit=False)
                generationClass.taskID = task
                generationClass.cateogaryTag = tag
                generationClass.save()
                tag += 1
            # return render(request, 'createtask/success.html')
            return redirect('createtask:Gen_example_add')

    return render(request, template_name, {
        'taskform': taskform,
        'formset': formset,
        'customform': customform,
    })


def AddGenExample(request):
    task = Task.objects.get(id=request.session['task'])
    # questionaire = Questionaire.objects.get(taskID=task) #try required
    class_list = task.cateogary_set.all()

    if request.method == 'GET':
        context = {'class_list': class_list}
        return render(request, 'createtask/addGenExamples.html', context)

    if request.method == 'POST':
        # for i in range(len(class_list)):
        #     input1 = request.POST['class'+i]
        #     exampleEntry =
        return render(request, 'createtask/success.html')

#TEXTGENERATION

def createTextGenerationTask(request):
    template_name = 'createtask/genarationTexttask_form.html'
    if request.method == 'GET':
        #customform = CustomForm1()
        taskform = CreateTaskForm(request.GET or None)
        csvform = CsvForm()
        #print(taskform.name.label)

    elif request.method == 'POST':
        print('woow')
        taskform = CreateTaskForm(request.POST)
        csvform = CsvForm(request.POST, request.FILES)
        # formset = CateogaryFormSet(request.POST)
        # customform = CustomForm1(request.POST)
        if taskform.is_valid() and csvform.is_valid():
            print('hell')
            task = taskform.save(commit=False)
            task.creatorID = UserNew2.objects.get(name='kasun')
            task.taskType = "TextGen"
            newFileModel = GenTextFile()
            task.save()
            newFileModel.taskID = task
            newFileModel.csvFile = request.FILES['data']
            newFileModel.save()
            filename = './'+newFileModel.csvFile.url
            processCsvGen(filename,task)
            request.session['task'] = task.id      #task id session created

            # return render(request, 'createtask/success.html')
            return redirect('createtask:Gen_example_add')
        else:
            print('aiiyo')
            #print(taskform.errors)
            print(csvform.errors)
    
    return render(request, template_name, {
        'taskform': taskform,
        'csvform': csvform,
    })

def processCsvGen(filename,task):
    with open(filename, "r") as f:
        reader = csv.reader(f, delimiter=",")
        instancelist = []
        for i, line in enumerate(reader):
            if i==0:
                continue
            else:
                data = line[0]
                print(line[0])
                DataGenTextinstance = DataGenTextInstance(taskID=task,data=data)
                instancelist.append(DataGenTextinstance)
        DataGenTextInstance.objects.bulk_create(instancelist)