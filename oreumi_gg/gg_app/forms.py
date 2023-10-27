from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget
from .models import BlogPost, Comment

class BlogPostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["content"].required = False        
    class Meta:
        model = BlogPost
        fields = ("title", "content")
        labels = {
            'title':'',
            'content':''
        } 
        widgets = {
            "title":forms.TextInput(attrs={'class': 'form-control', 'placeholder':'제목을 입력해주세요.'}),
            "content": CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"}, config_name="extends",
            )
        }








class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {
            'text': '',  # 'text' 필드의 라벨을 빈 문자열로 설정
        }

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({
            'class': 'form-comment',
            'rows': '4',
            'cols': '100',
        })