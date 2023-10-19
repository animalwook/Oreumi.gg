from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import BlogPostForm
# Create your views here.


def index(request):
    blog_post = BlogPost.objects.all()
    return render(request,"index.html",{"posts":blog_post})


def post(request):
    blog_post = BlogPost.objects.all().order_by('-created_at')  # 가장 최근에 생성된 게시글 먼저 나타남
    context = {"posts": blog_post}      
    return render(request, 'post.html', context)


def create_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()  # 폼이 유효하면 데이터베이스에 저장
            return redirect('gg_app:post')  # 게시글 목록 페이지로 리다이렉트
    else:
        form = BlogPostForm()  # GET 요청인 경우 빈 폼 생성

    return render(request, 'create_post.html', {'form': form})