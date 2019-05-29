from rest_framework import serializers
from .models import Profile,Project

class ProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = Profile
    fields ('name','profile_photo','bio')

class ProjectSerializer(serializers.ModelSerializer):
  class Meta:
    model = Project
    fields('author','name','description','img','link')
    
