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
class Review(models.Model):
   rev = models.CharField(max_length = 100,blank = True)
   design = models.IntegerField(blank = True)
   usability = models.IntegerField(blank=True)
   content = models.IntegerField(blank=True)
   rev_by = models.ForeignKey(User,on_delete=models.CASCADE)

def save_review(self):
   self.save()

def delete_review(self):
   comments.objects.get(id = self.id).delete()

def update_review(self,new_review):
   rev = Review.objects.get(id = self.id)
   rev.review= new_review
   rev.save()



