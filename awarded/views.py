from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required


def home(request):
    project = Project.objects.all()

    return render(request, 'index.html',context)

