from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'gg_app' 
 
urlpatterns = [
    path('', views.index, name='index'),
  
    path('community/', views.community, name='community'),
    path('champions/', views.champions, name='champions'),
    path('login/', views.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), # 장고 auth에서 logout 매서드 사용
    path('register/', views.register, name='register'),

    path('post/', views.post, name='post'),
    path('create/', views.post_create, name='post_create'),                  # create. post 원리 이해하기
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),      # 새로 추가한 URL 패턴), <int:post_id> 부분은 URL 패턴에서 변수를 캡처하는 부분
    path('post_edit/<int:post_id>/', views.post_edit, name='post_edit'),     # post_edit 수정 부분

    path('post/<int:post_id>/add_comment/', views.add_comment, name='add_comment'),

    
    # 전적 검색
    path('summoners_form', views.summoners_info_form, name='summoners_info_form'),
    path('summoners/<str:country>/<str:summoner_name>', views.summoners_info, name='summoners_info'),   #검색결과를 보여줄 화면
    # path('api/summoners_info/<str:country>/<str:summoner_name>/<int:count>/', views.summoners_info_api, name='summoners_info_api'),
]
