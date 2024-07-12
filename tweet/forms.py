from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo']
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'bg-black text-white p-2 rounded-lg w-full', 
                'placeholder': 'What\'s happening?',
                'style': 'resize: none;',
                'rows': 7,
            }),
        }
        
class UserRegisterationForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.TextInput(attrs={
            'class': 'bg-black text-white p-2 rounded-lg w-auto',
            'placeholder': 'Email'
        })
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={
            'class': 'bg-black text-white p-2 rounded-lg w-auto',
            'placeholder': 'Username'
        })
        self.fields['password1'].widget = forms.PasswordInput(attrs={
            'class': 'bg-black text-white p-2 rounded-lg w-auto',
            'placeholder': 'Password'
        })
        self.fields['password2'].widget = forms.PasswordInput(attrs={
            'class': 'bg-black text-white p-2 rounded-lg w-auto',
            'placeholder': 'Confirm Password'
        })

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'bg-black text-white p-2 my-2 rounded-lg w-auto',
            'placeholder': 'Username'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'bg-black text-white p-2 my-2 rounded-lg w-auto',
            'placeholder': 'Password'
        })
    )

class CustomEditProfileForm(forms.ModelForm):
    class Meta:
        model = TweetUserData
        fields = ['first_name', 'last_name', 'profile_Image', 'cover_Image', 'bio', 'birth_Date', 'instagram',]
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'bg-black text-white p-2 rounded-lg w-full',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'bg-black text-white p-2 rounded-lg w-full',
            }),
            'profile_Image': forms.ClearableFileInput(attrs={
                'class': 'bg-black text-white p-2 rounded-lg w-1/2',
            }),
            'cover_Image': forms.ClearableFileInput(attrs={
                'class': 'bg-black text-white p-2 rounded-lg w-1/2',
            }),
            'bio': forms.Textarea(attrs={
                'class': 'bg-black text-white p-2 rounded-lg w-full',
                'style': 'resize: none;',
                'rows': 5,
            }),
            'instagram': forms.TextInput(attrs={
                'class': 'bg-black text-white p-2 rounded-lg w-auto',
                'style': 'resize: none;',
            }),
            'birth_Date': forms.DateInput(attrs={
                'class': 'bg-black text-white p-2 rounded-lg w-auto',
                'type': 'date',
            }),
        }