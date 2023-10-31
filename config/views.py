from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout

def edu_login(request):
    context = {}
    print(request.method)
    if request.method=='POST':
        print(1)
        username = request.POST.get('login')
        password = request.POST.get('password')
        if username=='' or password=='':
            context['error'] = "Ma'lumot to'ldirilmadi"
            return render(request,'login.html',context)
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)  
            if len(user.groups.all().filter(name='Users'))!=0: 
                return redirect('home')
            elif  len(user.groups.all().filter(name='BallUser'))!=0: 
                return redirect('homeBall')
            elif  len(user.groups.all().filter(name='Uquv'))!=0: 
                return redirect('homeUquv')
            else:
                context['error'] = "Bu tizmga kirishga ruxsat berilmagan"
                return render(request,'login.html',context)
        else:
            context['error']='Login yoki parol xato'
    return render(request,'login.html',context)

def logout_user(request):
    logout(request)
    return redirect('edu_login')