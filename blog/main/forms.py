from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'is_published', 'category', 'image']
        widgets = {
            'category': forms.Select(attrs={'class': 'custom-select'}),
            'image': forms.ClearableFileInput(attrs={'class': 'custom-file-input'}),
        }