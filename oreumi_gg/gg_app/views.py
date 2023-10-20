from django.shortcuts import render, redirect,  get_object_or_404
from .models import BlogPost
from .forms import BlogPostForm
# Create your views here.


def index(request):
    blog_post = BlogPost.objects.all()
    return render(request,"index.html",{"posts":blog_post})

# 게시판 목록
def post(request):
    blog_post = BlogPost.objects.all().order_by('-created_at')  # 가장 최근에 생성된 게시글 먼저 나타남
    context = {"posts": blog_post}      
    return render(request, 'post.html', context)


# 게시글 작정
def post_create(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()  # 폼이 유효하면 데이터베이스에 저장
            return redirect('gg_app:post')  # 게시글 목록 페이지로 리다이렉트
    else:
        form = BlogPostForm()  # GET 요청인 경우 빈 폼 생성

    return render(request, 'post_create.html', {'form': form})


# 게시글 수정
def post_edit(request, post_id):        
    post = BlogPost.objects.get(pk=post_id)

    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('gg_app:post')  # 수정 후 게시물 목록 페이지로 리디렉션
    else:
        form = BlogPostForm(instance=post)

    return render(request, 'post_edit.html', {'form': form, 'post': post})


# 상세 페이지
def post_detail(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)  # 게시물 가져오기, 없으면 404 에러 발생
    return render(request, 'post_detail.html', {'post': post})