from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget
from .models import BlogPost, Comment

class BlogPostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["content"].required = False        
    class Meta:
        model = BlogPost
        fields = ("title", "content",'category')
        widgets = {
            "content": CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"}, config_name="extends",
            )
        }








class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
