from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UserChangeForm
from django.core.validators import RegexValidator
from .models import User,Product

class contactform(UserCreationForm):
    password=None
    class Meta:
        model=User
        fields=['username','phone','email','password1','password2']
class loginform(AuthenticationForm):
    phone_no=forms.CharField(min_length=4)
    class Meta:
        model=User
        fields=['phone','email','password1']
class userchangeform(UserChangeForm):
    password = forms.PasswordInput()
    class Meta:
        model=User
        # fields=['username','email','password']              #'__all__'
        exclude=['username']
'''class contactform(forms.Form):
    name = forms.CharField(min_length=5, max_length=10, required=True)
    email = forms.EmailField(required=True)
    regex_phone = RegexValidator(regex=r'^\+?1?\d{10}$', message='10digit phone number required')
    phone = forms.CharField(max_length=255, required=True, validators=[regex_phone])
    query = forms.CharField(widget=forms.Textarea)
    password = forms.CharField(min_length=4, max_length=8, widget=forms.PasswordInput)
'''