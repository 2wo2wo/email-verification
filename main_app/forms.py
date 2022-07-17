from django import forms
from django.contrib.auth import get_user_model
from .models import UserModel

class ContactForm(forms.Form):
    subject = forms.CharField(required=True)
    from_email = forms.EmailField(required=True)
    messsage = forms.CharField(widget=forms.Textarea, required=True)


# User = get_user_model()


class UserForm(forms.Form):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    password1 = forms.CharField(widget=forms.PasswordInput, required=True)
