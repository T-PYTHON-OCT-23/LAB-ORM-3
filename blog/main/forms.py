from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'is_published', 'category', 'image']
        widgets = {
            'category': forms.Select(attrs={'class': 'custom-select'}),
            'image': forms.ClearableFileInput(attrs={'class': 'custom-file-input'}),
        }


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required. Enter your first name.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required. Enter your last name.')
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User 
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email')