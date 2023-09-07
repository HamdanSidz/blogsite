from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from .models import Post


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))
    email = forms.EmailField(required=True,widget = forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email address'}))  # THIS field is not required in models user creation so here it is made required in forms by overwriting it


    class Meta:
        model = User

        fields = ["username", "first_name", "last_name",
                  "email"]

        widgets = {'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
                   'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First name'}),
                   'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last name'}),
                   }


class Loginform(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": "User name"}))
    password = forms.CharField(strip=False, widget=forms.PasswordInput(
        attrs={"class": "form-control", "placeholder": "Password"}))


class Post_form(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "desc"]
        widgets = {"title": forms.TextInput(attrs={'class': 'form-control'}),
                   "desc": forms.Textarea(attrs={'class': 'form-control',"rows":3}),
                   }


class Comments_form(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["desc"]
        widgets = {"desc": forms.Textarea(attrs={'class': 'form-control','placeholder': 'Add Comment',"rows":1})}





