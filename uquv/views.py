from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from api.models import *


@login_required
def homeView(requests):
    context = {}
    get_list = []
    lists = []
    get_user = User.objects.prefetch_related('groups').filter(groups__name__in = ['Users'])
    for i in get_user:
        
        get_ball = PutBall.objects.select_related('user').filter(user = i.id)
        # print(get_ball)
        for k in get_ball: 
            lists.append({
                    'ball': k.ball / len(k.question_id.question_id.put_ball.all()),
                    'name':i.first_name +" "+i.last_name,
                })            
        # print(lists)
    
    aggregated_data = {}
                
    for dictionary in lists:
        key = (dictionary['name'])
            
        aggregated_data[key] = aggregated_data.get(key, 0) + dictionary['ball']
                
    get_list = [{'name': key, 'ball': value} for key, value in aggregated_data.items()]  
    
    return render(requests, 'uquv/index.html', {'get_list':list(get_list)})