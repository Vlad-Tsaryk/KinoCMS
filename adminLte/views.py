from django.db.models import Count
from django.shortcuts import render
from users.models import User
from cinema.models import Session
import datetime


# Create your views here.
def statistic(request):

    obj_users = User.objects.all()
    today = datetime.date.today()
    last_month = today.replace(month=today.month - 1)
    print(last_month)
    sessions = Session.objects.filter(date_time__gte=last_month) \
        .values('date_time__day', 'date_time__month', 'date_time__year') \
        .annotate(dcount=Count('date_time')).order_by('date_time__day')
    print(sessions)
    sessions_days = []
    sessions_count = []
    for s in sessions:
        # print('day: '+str(s['date_time__day'])+'//// month: '+str(s['date_time__month']))
        print(s)
        sessions_count.append(s['dcount'])
        sessions_days.append(s['date_time__day'])
    # print(sessions.values('date_time__day'))
    users_gender_count = obj_users.values('gender').annotate(count=Count('gender'))

    context = {'obj_users': obj_users, 'sessions_count': sessions_count, 'sessions_days': sessions_days,
               'gender': users_gender_count}
    return render(request, 'adminLte/statistic.html', context)
