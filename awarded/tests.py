from django.test import TestCase

from django.test import TestCase
from .models import Profile,Posts,tag

class ProfileTestClass(TestCase):
    def setUp(self):
        self.rehema = Profile(first_name = 'Rehema',last_name='Wasike',username='fefe',email='rehemafaith01@gmail.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.rehema,Profile))

    def test_save(self):
        self.rehema.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)>0)
 

 class ProjectTestClass(TestCase):
    def setUp(self):
        self.rehema = Profile(first_name = 'Rehema',last_name='Rehema',username='fefe',email='rehemafaith01@gmail.com')
        self.rehema.save_profile()

       
        self.new_post =Project(caption="testing testing 1,2",profile=self.rehema)
        self.new_post.save()

        self.new_post.tag.add(self.new_tag)

    def tearDown(self):
        Profile.objects.all().delete()
     
        Project.objects.all().delete()    

    def test_posts(self):
        posts = Project.posts()
        self.assertTrue(len(posts)>0)
