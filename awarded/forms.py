from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import Profile,Project,Review





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

   rev = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Review'}))
   design = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Design'}))
   Usability = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Usability'}))
   Content = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Content'}))
   
