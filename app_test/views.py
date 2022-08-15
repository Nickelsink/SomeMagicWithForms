from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from app_test.models import Man


def my_first_view(request):
    people = Man.objects.all()
    return render(request, 'index.html', {'people': people})


def my_second_view(request):
    if request.method == "POST":
        man = Man.objects.get(id=request.POST['id'])
        man.is_allowed = True
        man.save()
        return HttpResponseRedirect(reverse("first_view"))
    return HttpResponse("Вторая страница")
