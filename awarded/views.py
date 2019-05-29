from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Profile,Project,Review
from .forms import ProjectForm,ReviewForm
from django.db.models import Sum 
from django.http import JsonResponse

@login_required(login_url='/accounts/login/')
def home(request):
    project = Project.objects.all()

    return render(request, 'layout.html',{'project':project})

@login_required(login_url='/accounts/login/')
def profile(request):
   profile = Profile.objects.all()

   return render (request,'profile.html',{"profile":profile})


@login_required(login_url='/accounts/login/')
def new_project(request):

   current_user = request.user
   if request.method == 'POST':
      form = ProjectForm(request.POST,request.FILES)
      if form.is_valid():
         project = form.save(commit=False)
         project.author = current_user
         form.save()
         return redirect('home')
   else:
      form = ProjectForm()

   

   return render(request, 'project_form.html',{'form':form})



@login_required(login_url='/accounts/login/')
def full_project(request):
   current_user=request.user
   project = Project.objects.all()
   
   current_user = request.user
   if request.method == 'POST':
      form = ReviewForm(request.POST,request.FILES)
      if form.is_valid():
         review = form.save(commit=False)
         review.rev_by = current_user
         form.save()
         return redirect('project')
   else:
      form = ReviewForm

   return render(request, 'projects.html',{'project':project})
