from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import Profile,Project,Review,Comments





class ProjectForm(forms.ModelForm):
   '''
   New project creation form.
   '''

   name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Project Title'}))
   description = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Description'}))
   link = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Project Link'}))
   description = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Project Description'}))

   class Meta:
      model = Project
      fields = ['name','img','description','link']

class ReviewForm(forms.ModelForm):
   '''
   Review Form
   '''
  
   class Meta:
      model = Review
      fields =['usability','design','content']

class CommentForm(forms.ModelForm):

      class Meta:
        model = Comments
        fields = ('comments',)