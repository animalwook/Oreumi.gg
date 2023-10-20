from django.urls import path
from . import views
 
app_name = 'gg_app'    #score 어플리케이션의 url 호출시 앞의 구분자 사용을 하시려면 작성합시다.
 
urlpatterns = [
    path('', views.index, name='index'),
    path('community/', views.community, name='community'),
    path('champions/', views.champions, name='champions'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),

    # 전적 검색
    path('summoners_form', views.summoners_info_form, name='summoners_info_form'),
    path('summoners/<str:country>/<str:summoner_name>', views.summoners_info, name='summoners_info'),   #검색결과를 보여줄 화면
]