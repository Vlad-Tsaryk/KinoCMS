from django.shortcuts import render


# Create your views here.
def statistic(request):
    context = {}
    return render(request, 'adminLte/statistic.html', context)
