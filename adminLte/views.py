from django.shortcuts import render
from users.models import User


# Create your views here.
def statistic(request):
    print(request.session)
    obj_users = User.objects.all()
    context = {'obj_users': obj_users}
    return render(request, 'adminLte/statistic.html', context)
