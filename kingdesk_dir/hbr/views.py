from django.shortcuts import render, redirect
from aup.models import Employers, Current_shedules, Months, Current_tasks, Future_shedules, Posts, Divisions, Future_shedules_New_Year, Week_days, Wishes
from django.views.generic import DetailView
from datetime import datetime, timedelta
from django.contrib.auth.models import User

def wishes(request):
    employers = Employers.objects.order_by('surname')
    hbr_employers = ['h-01', 'h-02', 'h-03', 'h-04', 'h-05']
    aup_employers = ['a-01', 'a-02', 'a-03']
    wishes = Wishes.objects.all()
    user = None
    for i in employers:
        if i.username == request.user.username:
            user = i
            break
    return render(request, 'hbr/wishes.html', {'user':user, 'employers':employers, 'hbr_employers':hbr_employers, 'aup_employers':aup_employers, 'wishes':wishes})  


def send_wish(request, user_id):
    wishes = Wishes.objects.all()
    employers = Employers.objects.order_by('surname')
    for i in employers:
        if i.id == user_id:
            wish = Wishes()
            wish.employer_from = i.surname + ' ' + i.name
            wish.wish = request.POST.get('message')
            wish.employer_to = request.POST.get('employer_to')
            wish.save()
            print()
            break
    
    return redirect ('hbr_wishes') 



def my_current_shedule(request):
    hbr_employers = ['h-01', 'h-02', 'h-03', 'h-04', 'h-05']
    aup_employers = ['a-01', 'a-02', 'a-03']
    employers = Employers.objects.all()
    current_shedules = Current_shedules.objects.all()
    months = Months.objects.all()
    ctd = Current_tasks.objects.all()
    user = None
    for i in employers:
        if i.username == request.user.username:
            user = i
            break
    return render(request, 'hbr/my_current_shedule.html', {'user':user, 'employers':employers, 'current_shedules': current_shedules, 'months':months, 'hbr_employers':hbr_employers, 'aup_employers':aup_employers, 'ctd':ctd})  
        
def our_current_shedule(request):
    date_now = datetime.now().date() + timedelta(hours=5)
    tomorrow  = date_now + timedelta(1)
    hbr_employers = ['h-01', 'h-02', 'h-03', 'h-04', 'h-05']
    aup_employers = ['a-01', 'a-02', 'a-03']
    employers = Employers.objects.order_by('surname')
    current_shedules = Current_shedules.objects.all()
    months = Months.objects.all()
    user = None
    for i in employers:
        if i.username == request.user.username:
            user = i
            break
    return render(request, 'hbr/our_current_shedule.html', {
        'user':user, 
        'employers':employers, 
        'current_shedules':current_shedules, 
        'months':months, 
        'hbr_employers':hbr_employers, 
        'aup_employers':aup_employers, 
        'date_now':date_now,
        'tomorrow':tomorrow
        })
        
def profile(request):
    hbr_employers = ['h-01', 'h-02', 'h-03', 'h-04', 'h-05']
    aup_employers = ['a-01', 'a-02', 'a-03']
    employers = Employers.objects.order_by('surname')
    user = None
    for i in employers:
        if i.username == request.user.username:
            user = i
            break
    return render(request, 'hbr/profile.html', {'user':user, 'employers':employers, 'hbr_employers':hbr_employers, 'aup_employers':aup_employers})

def edit_profile(request):
    hbr_employers = ['h-01', 'h-02', 'h-03', 'h-04', 'h-05']
    aup_employers = ['a-01', 'a-02', 'a-03']
    employers = Employers.objects.order_by('surname')
    posts = Posts.objects.order_by('post_name')
    divisions = Divisions.objects.order_by('division_name')
    user = None
    for i in employers:
        if i.username == request.user.username:
            user = i
            break
    return render(request, 'hbr/edit_profile.html', {'user':user, 'employers':employers, 'hbr_employers':hbr_employers, 'aup_employers':aup_employers, 'posts':posts, 'divisions':divisions})

def update_profile(request, user_id):
    try:
        if request.method == "POST":
            user = Employers.objects.get(id=user_id)

            user.surname = request.POST.get("surname")
            user.name = request.POST.get("name")
            user.lastname = request.POST.get("lastname")
            user.phone = request.POST.get("phone")
            if user.password != request.POST.get("password"):
                user.password = request.POST.get("password")
                user.save()
                user_2 = User.objects.get(username = user.username)
                user_2.delete() 
                User.objects.create_user(username=user.username, password=user.password)
            else:
                user.save()
        return redirect ('hbr_profile')
    except:
        return redirect ('hbr_edit_profile')

def employers(request):
    hbr_employers = ['h-01', 'h-02', 'h-03', 'h-04', 'h-05']
    aup_employers = ['a-01', 'a-02', 'a-03']
    employers = Employers.objects.order_by('surname')
    user = None
    for i in employers:
        if i.username == request.user.username:
            user = i
            break
    return render(request, 'hbr/employers.html', {'user':user, 'employers':employers, 'hbr_employers':hbr_employers, 'aup_employers':aup_employers})

class Employer_Detail_View(DetailView):
    model = Employers
    template_name = 'hbr/employer_info.html'
    context_object_name = 'employer'

def future_shedule(request):
    hbr_employers = ['h-01', 'h-02', 'h-03', 'h-04', 'h-05']
    aup_employers = ['a-01', 'a-02', 'a-03']
    employers = Employers.objects.order_by('surname')
    future_shedules = Future_shedules.objects.all()
    months = Months.objects.all()
    user = None
    for i in employers:
        if i.username == request.user.username:
            user = i
            break
    return render(request, 'hbr/future_shedule.html', {'user':user, 'employers':employers, 'future_shedules':future_shedules, 'months':months, 'hbr_employers':hbr_employers, 'aup_employers':aup_employers})
 
def future_shedule_hny(request):
    hbr_employers = ['h-01', 'h-02', 'h-03', 'h-04', 'h-05']
    aup_employers = ['a-01', 'a-02', 'a-03']
    employers = Employers.objects.order_by('surname')
    future_shedules = Future_shedules_New_Year.objects.all()
    months = Months.objects.all()
    user = None
    for i in employers:
        if i.username == request.user.username:
            user = i
            break
    return render(request, 'hbr/future_shedule_hny.html', {'user':user, 'employers':employers, 'future_shedules':future_shedules, 'months':months, 'hbr_employers':hbr_employers, 'aup_employers':aup_employers})

def edit_shedule(request, user_id):
    future_shedules = Future_shedules.objects.all()
    for i in future_shedules:
        if request.POST.get("date") == str(i.date.day) + ' ' + str(i.date.month) and user_id == i.employer_id.id:
            id = i.id
            break
    shedule = Future_shedules.objects.get(id=id)
    try:
        if request.method == "POST":
            if request.POST.get("is_weekend") == 'on':
                shedule.is_weekend = True
                shedule.start_work = '00:00:00'
                shedule.end_work = '00:00:00'
            else:
                shedule.is_weekend = False
                shedule.start_work = request.POST.get("start_work")
                shedule.end_work = request.POST.get("end_work")
            shedule.comment = request.POST.get("comment")
            shedule.save()
        return redirect ('hbr_fs')
    except:
        return redirect ('hbr_fs')      
    
def edit_shedule_hny(request, user_id):
    future_shedules = Future_shedules_New_Year.objects.all()
    for i in future_shedules:
        if request.POST.get("date") == str(i.date.day) + ' ' + str(i.date.month) and user_id == i.employer_id.id:
            id = i.id
            break
    shedule = Future_shedules_New_Year.objects.get(id=id)
    try:
        if request.method == "POST":
            if request.POST.get("is_weekend") == 'on':
                shedule.is_weekend = True
                shedule.start_work = '00:00:00'
                shedule.end_work = '00:00:00'
            else:
                shedule.is_weekend = False
                shedule.start_work = request.POST.get("start_work")
                shedule.end_work = request.POST.get("end_work")
            shedule.comment = request.POST.get("comment")
            shedule.save()
        return redirect ('hbr_fs_hny')
    except:
        return redirect ('hbr_fs_hny')  

def abra(request, division_id):
    current_shedules = Current_shedules.objects.all()
    future_shedules = Future_shedules_New_Year.objects.all()
    division = Divisions.objects.get(id=division_id)

    for i in current_shedules:
        if i.employer_id.division_id.id == division_id:
            future_shedule = Future_shedules_New_Year()
            future_shedule.week_day_id = Week_days.objects.get(id=i.week_day_id.id)
            future_shedule.date = i.date + timedelta(7)
            future_shedule.employer_id = Employers.objects.get(id=i.employer_id.id)
            future_shedule.start_work = '00:00:00'
            future_shedule.end_work = '00:00:00'
            future_shedule.is_weekend = True
            future_shedule.comment = ''
            future_shedule.save()
    for i in current_shedules:
        if i.employer_id.division_id.id == division_id:
            future_shedule = Future_shedules_New_Year()
            future_shedule.week_day_id = Week_days.objects.get(id=i.week_day_id.id)
            future_shedule.date = i.date + timedelta(14)
            future_shedule.employer_id = Employers.objects.get(id=i.employer_id.id)
            future_shedule.start_work = '00:00:00'
            future_shedule.end_work = '00:00:00'
            future_shedule.is_weekend = True
            future_shedule.comment = ''
            future_shedule.save()
    for i in current_shedules:
        if i.employer_id.division_id.id == division_id:
            future_shedule = Future_shedules_New_Year()
            future_shedule.week_day_id = Week_days.objects.get(id=i.week_day_id.id)
            future_shedule.date = i.date + timedelta(21)
            future_shedule.employer_id = Employers.objects.get(id=i.employer_id.id)
            future_shedule.start_work = '00:00:00'
            future_shedule.end_work = '00:00:00'
            future_shedule.is_weekend = True
            future_shedule.comment = ''
            future_shedule.save()
    return redirect ('hbr_fs_hny')

