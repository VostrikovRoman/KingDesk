from django.shortcuts import render, redirect
from django.http import HttpResponse
from aup.models import Employers
from django.contrib.auth import authenticate, login, logout


def sign_in(request):
    hbr_employers = ['h-01', 'h-02', 'h-03', 'h-04', 'h-05']
    aup_employers = ['a-01', 'a-02', 'a-03']
    try:
        if request.user.is_authenticated:
            employers = Employers.objects.all()
            for i in employers:
                if request.user.username == i.username and i.post_id.post_code in hbr_employers:
                    return redirect ('hbr_mcs')
                elif request.user.username == i.username and i.post_id.post_code in aup_employers:
                    return redirect ('aup_cs')
        else:
            return render(request, 'sign_in/sign_in.html')
    except:
        return render(request, 'sign_in/sign_in.html')

def user_login (request):
    hbr_employers = ['h-01', 'h-02', 'h-03', 'h-04', 'h-05']
    aup_employers = ['a-01', 'a-02', 'a-03']
    
    try: 
        if request.POST:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user=user)
                employers = Employers.objects.all()
                for i in employers:
                    if user.username == i.username and i.post_id.post_code in hbr_employers:
                        return redirect ('hbr_mcs')
                    elif user.username == i.username and i.post_id.post_code in aup_employers:
                        return redirect ('aup_cs')
            else: 
                return redirect('sign_in')
    except:
        return redirect('sign_in')
    
def user_logout (request):
    logout(request)
    return redirect('sign_in')

