from django.shortcuts import render, reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from api.models import *

# Create your views here.
@login_required
def homeView(requests):
    context = {}
    context['list_main_cate'] = []
    for i in MainCategories.objects.all():
        filter_category = Categories.objects.prefetch_related('main_categories_id').filter(main_categories_id = i)
        context['list_main_cate'].append({'name':i.name,'ball_of_cate':i.ball_of_cate,'id':i.id,'cate': filter_category})
    return render(requests, 'ball/index.html', context)


@login_required
def questionView(requests, id):
    context = {}
    queryset = get_object_or_404(Categories, id = id)
    context['question'] = Questions.objects.select_related('categories_id').filter(categories_id = queryset)
    context['lists'] = []
    for k in context['question']:
        filter_file_upload = FileUpload.objects.select_related('question_id').filter(question_id = k.id)
        
            
        context['lists'] .append({
            'id':k.id ,
            'question':k.question ,
            'date_of_calculation_ball':k.date_of_calculation_ball ,
            'ball_of_question':k.ball_of_question ,
            'description':k.description ,
            'categories_id':k.categories_id ,
            'description1':k.description1 ,
            'filter_file_upload':filter_file_upload
        })

    return render(requests, 'ball/questions.html', context)


@login_required
def file_uploadView(requests, id):
    context = {}
    context['queryset'] = get_object_or_404(FileUpload, id=id)
    ids = context['queryset'].question_id.categories_id.id
    
    if requests.method == 'POST':
        number = requests.POST.get('number')
        if number == '':
            context['error'] = "Ma'lumot to'ldirilmadi, qayta urinib ko'ring..."
            return render(requests, 'ball/file_upload.html',context)
        if int(number) > int(context['queryset'].question_id.ball_of_question) or int(number) <= 0:
            context['error'] = "Yuqaridagi balldan o'tib ketmasin, qayta urinib ko'ring..."
            return render(requests, 'ball/file_upload.html',context)
        
        create = PutBall.objects.create(
            ball = number,
            user = context['queryset'].author,
            question_id = context['queryset'],
            author = requests.user,
        )
        context['queryset'].add_ball.add(requests.user)
        context['queryset'].save()
        if len(context['queryset'].question_id.put_ball.all()) == len(context['queryset'].add_ball.all()):
            context['queryset'].is_activte = True
            context['queryset'].save()
            
        return HttpResponseRedirect(reverse('questionsBall', args=(ids, ))) 
    
    return render(requests, 'ball/file_upload.html',context)


@login_required
def repition_ball(requests, id):
    context = {}
    context['queryset'] = get_object_or_404(FileUpload, id=id)
    ids = context['queryset'].question_id.categories_id.id
    
    # print(context['queryset'])
    files_get = PutBall.objects.select_related('author').filter(
        author = requests.user
    ).select_related('user').filter(
        user = context['queryset'].author.id
    ).select_related('question_id').filter(
        question_id = context['queryset'].id
    )[0]
   
    if requests.method == 'POST':
        files = requests.FILES.get('file', None)
        number = requests.POST.get('number')
        
        if files == None or number == "":
            context['error'] = "Fayl yuklanmadi yoki Baholanmadi, qayta urinib ko'ring..."
            return render(requests, 'ball/repo.html',context)
        
        if int(number) >= 0:
            context['error'] = "Baho Qaytarilsin, qayta urinib ko'ring..."
            return render(requests, 'ball/repo.html',context)
            
        create = Repetition.objects.create(
            ball = number,
            user = context['queryset'].author,
            question_id = context['queryset'],
            author = requests.user,
            files = files
        )
    
        files_get.ball = files_get.ball + int(number)
        files_get.save()
        context['queryset'].repition_ball.add(requests.user)
        context['queryset'].save()
        return HttpResponseRedirect(reverse('questionsBall', args=(ids, )))
    
    return render(requests, 'ball/repo.html',context)
        
        

@login_required
def portfolioViews(requests):
    context = {}
    context['queryset'] = Repetition.objects.select_related('author').filter(
        author = requests.user
    )
    return render(requests, 'ball/repo_get.html', context)