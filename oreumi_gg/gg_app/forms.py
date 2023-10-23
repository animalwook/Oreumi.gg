from django import forms
from .models import BlogPost


class PostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content']




class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'author', 'category']  # 'image' 필드 추가


