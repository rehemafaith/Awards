from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Profile,Project


def home(request):
    project = Project.objects.all()

    return render(request, 'index.html',{'project':project})

def new_project(request):

   user = request.user
   if request.method == 'POST':
      form = ProjectForm(request.POST,request.FILES)
      if form.is_valid():
         project = form.save(commit=False)
         project.author = user.profile
         project.save()
         return redirect('home')
   else:
      form = ProjectForm()

   

   return render(request, 'rate/new_project.html',{'form':form})