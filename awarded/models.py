from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
   '''
   Holds user's profile data.
   '''

   name = models.CharField(max_length = 250)
   profile_photo = models.ImageField(upload_to = "images/")
   bio = models.TextField()

   def save_profile(self):
    self.save()
  
   def delete(self):
    Profile.objects.get(id = self.id).delete()
  
   def update(self,field,val):
    Profile.objects.get(id=self.id).update(field=val)
    

   def __str__(self):
      return self.name

class Project(models.Model):
   '''
   Model to hold user's project data.
   '''

   author = models.ForeignKey(User, on_delete=models.CASCADE)
   name = models.CharField(max_length=70)
   description = models.TextField(max_length=140)
   img = models.ImageField(upload_to='projects/')
   link = models.CharField(max_length=140)


   
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
