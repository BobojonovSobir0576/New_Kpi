from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from .models import *


@login_required
def homeView(requests):
    context = {}
    context['list_main_cate'] = []
    for i in MainCategories.objects.all():
        filter_category = Categories.objects.prefetch_related('main_categories_id').filter(main_categories_id = i)
        context['list_main_cate'].append({'name':i.name,'ball_of_cate':i.ball_of_cate,'id':i.id,'cate': filter_category})
    return render(requests, 'user/index.html', context)

@login_required
def questionView(requests, id):
    context = {}
    queryset = get_object_or_404(Categories, id = id)
    context['question'] = Questions.objects.select_related('categories_id').filter(categories_id = queryset)
    context['lists'] = []
    for i in context['question']:
        filter_file_upload = FileUpload.objects.select_related('question_id').filter(question_id = i.id).select_related(
            'author'
        ).filter(author = requests.user)
        context['lists'].append({
            'id':i.id ,
            'question':i.question ,
            'date_of_calculation_ball':i.date_of_calculation_ball ,
            'ball_of_question':i.ball_of_question ,
            'description':i.description ,
            'categories_id':i.categories_id ,
            'description1':i.description1 ,
            'filter_file_upload':bool(filter_file_upload)
        })
    return render(requests, 'user/quiz.html', context)


@login_required
def file_uploadView(requests, id):
    context = {}
    context['queryset'] = get_object_or_404(Questions, id=id)
    
    ids = context['queryset'].categories_id.id
    
    if requests.method == 'POST':
        files = requests.FILES.get('file', None)

        if files == None:
            context['error'] = "Fayl yuklanmadi, qayta urinib ko'ring..."
            return render(requests, 'user/file_upload.html',context)
        
        create = FileUpload.objects.create(
            files = files,
            author = requests.user,
            question_id = context['queryset']
        )
        context['queryset'].add_user.add(requests.user.id)
        context['queryset'].save()
        context['msg'] = "Fayl Yuklandi..."
        # return render(requests, 'user/file_upload.html',context)
        return HttpResponseRedirect(reverse('questions', args=(ids, )))
    
    return render(requests, 'user/file_upload.html',context)


@login_required
def portfolioView(requests):
    
    context = {}
    context['queryset']= FileUpload.objects.filter(author = requests.user)
    context['lists'] = []
    for k in context['queryset']:
        get_put = PutBall.objects.select_related('author').filter(author__id__in=k.add_ball.all()).select_related('question_id').filter(question_id = k.id)
        repo = Repetition.objects.select_related('author').filter(author__id__in=k.add_ball.all()).select_related('question_id').filter(question_id = k.id)
        
        s=0
        for i in get_put:
            s+=i.ball/len(k.add_ball.all())
        context['lists'].append({
            'id':k.id ,
            'author':k.author ,
            'question_id':k.question_id ,
            'files':k.files ,
            'is_activte':k.is_activte ,
            'add_ball':k.add_ball ,
            'created_date':k.created_date ,
            'get_put_ball':get_put ,
            'sums':s,
            'repo':repo,
        })
    
        #     for l in PutBall.objects.select_related('question_id').filter(question_id__question_id = k.question_id.id ).select_related('user').filter(user = requests.user).select_related('author').filter(author = i.id):
        #         print(l)
    return render(requests, 'user/portfolio.html',context)