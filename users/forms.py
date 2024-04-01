from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


# Creation of user
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
        
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        

#* This sections is to update info
# allow to update username and email
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
        
    class Meta:
        model = User
        fields = ['username', 'email']   
        
# allow to the image        
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
        