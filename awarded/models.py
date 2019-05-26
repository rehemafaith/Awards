from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
   '''
   Holds user's profile data.
   '''

   user = models.OneToOneField(User, on_delete=models.CASCADE)
   avatar = models.ImageField(upload_to='avatars/',null=True,default='default.jpg')
   bio = models.TextField(max_length=140,null=True)

   def __str__(self):
      return self.user.username

class Techused(models.Model):
   '''
   Holds data for the programming languages used.
   '''

   techused = models.CharField(max_length=50)

   def __str__(self):
      return self.language

class Project(models.Model):
   '''
   Model to hold user's project data.
   '''

   author = models.ForeignKey(Profile, on_delete=models.CASCADE)
   name = models.CharField(max_length=70)
   description = models.TextField(max_length=140)
   img = models.ImageField(upload_to='projects/')
   link = models.CharField(max_length=140)
   techused = models.ManyToManyField(Techused)
   
   def __str__(self):
      return self.name
      
class Rating(models.Model):
   '''
   Model to hold projects' ratings
   '''
   review = models.CharField(max_length=140,default='')
   design = models.IntegerField(default=0)
   usability = models.IntegerField(default=0)
   content = models.IntegerField(default=0)
   rated = models.ForeignKey(Project, on_delete=models.CASCADE)
   rated_by = models.ForeignKey(Profile, on_delete=models.CASCADE)

   def __str__(self):
      return self.rated.name
