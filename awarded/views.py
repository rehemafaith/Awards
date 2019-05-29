from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Profile,Project,Review,Comments
from .forms import ProjectForm,ReviewForm,CommentForm
from django.db.models import Sum 
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer,ProjectSerializer
from .permissions import IsAdminOrReadOnly


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
def full_project(request,project_id):
  
    project = Project.objects.get(id=project_id)
    all = Review.objects.filter(project=project_id) 
    print(all)
 
    
    # single user votes count
    count = 0
    for i in all:
        count+=i.usability
        count+=i.design
        count+=i.content
    
    if count > 0:
        average = round(count/3,1)
    else:
        average = 0
        
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = request.user
            rate.project = project_id
            rate.save()
        return redirect('project',project_id)
        
    else:
        form = ReviewForm() 
        
    # The votes logic
    votes = Review.objects.filter(project=project_id)
    usability = []
    design = []
    content = [] 
    
    for i in votes:
        usability.append(i.usability)
        design.append(i.design)
        content.append(i.content) 
        
    if len(usability) > 0 or len(design)>0 or len(content)>0:
        average_usability = round(sum(usability)/len(usability),1) 
        average_design = round(sum(design)/len(design),1)
        average_content = round(sum(content)/len(content),1) 
            
        average_rating = round((average_content+average_design+average_usability)/3,1) 
    
    else:
        average_content=0.0
        average_design=0.0
        average_usability=0.0
        average_rating = 0.0
        
    '''
    To make sure that a user only votes once
    '''
    
    arr1 = []
    for use in votes:
        arr1.append(use.user_id) 
                
    auth = arr1
       
    reviews = CommentForm(request.POST)
    if request.method == 'POST':
        
        if reviews.is_valid():
            comment = reviews.save(commit=False)
            comment.user = request.user
            comment.save()
            return redirect ('project',project_id)
        else:
            reviews = CommentForm()
            
        
    user_comments = Comments.objects.filter(pro_id=project_id)
       
    context = {
        'project':project,
        'form':form,
        'usability':average_usability,
        'design':average_design,
        'content':average_content,
        'average_rating':average_rating,
        'auth':auth,
        'all':all,
        'average':average,
        'comments':user_comments,
        'reviews':reviews,
        
    }
    
    return render(request,'projects.html',context) 


class ProjectList(APIView):
   def get(self,request,format=None):
      all_proj = Project.objects.all()
      serializers = ProjectSerializer(all_proj,many=True)

      return Response(serializers.data)
      permission_classes = (IsAdminOrReadOnly,)
   def post(self,request,format=None):
      serializers = ProjectSerializer(data=request.data)
      if serializers.is_valid():
         serializers.save()
         return Response(serializers.data, status=status.HTTP_201_CREATED)
         return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
         
         permission_classes = (IsAdminOrReadOnly,)
      
class ProfileList(APIView):
   def get(self,request,format=None):
      all_prof = Profile.objects.all()
      seerializers = ProfileSerializer(all_prof,many=True)
      return Response(serializers.data)

   def post(self,request,format=None):
      serializers = ProfileSerializer(data=request.data)
      if serializers.is_valid():
         serializers.save()
         return Response(serializers.data, status=status.HTTP_201_CREATED)
         return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
         
         permission_classes = (IsAdminOrReadOnly,)
      

