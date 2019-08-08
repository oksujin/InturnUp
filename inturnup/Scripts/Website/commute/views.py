from django.shortcuts import render, redirect
from user.models import Uniuser
from .models import Commute
from django.core.paginator import Paginator


def commute_record(request):
    if not request.session.get('user'):
        return redirect('/user/login/')
    elif request.method == "POST":
        user = Uniuser()
        user.save()
    return render(request, 'commute.html')


def commute_list(request):
    all_commutes = Commute.objects.all().order_by('-id')
    page = int(request.GET.get('p', 1))
    paginator = Paginator(all_commutes, 10)

    boards = paginator.get_page(page)
    return render(request, 'commute_list.html', {'commutes': commutes})
