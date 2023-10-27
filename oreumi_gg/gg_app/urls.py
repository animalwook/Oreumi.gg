from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'gg_app' 
 
urlpatterns = [
    path('', views.index, name='index'),
    path('modes/', views.modes, name='modes'),


    # 통계
    path('statistics_champions/', views.statistics_champions, name='statistics_champions'),
    path('statistics_tier/', views.statistics_tier, name='statistics_tier'),

    # 랭킹
    path('leaderboards/', views.leaderboards, name='leaderboards'),
    path('type_champions/', views.type_champions, name='type_champions'),
    path('type_ladder_flex/', views.type_ladder_flex, name='type_ladder_flex'),
    path('type_ladder/', views.type_ladder, name='type_ladder'),
    path('type_level/', views.type_level, name='type_level'),

    #커뮤니티, 글 작성
    #post_list가 첫화면이고 base_community는 block을 이용한 템플릿제공
    path('community/main/', views.community, name='community'),
    path('community/main/<str:category>/<str:order_by>/', views.community, name='community'),

    path('community/post/<int:post_id>/', views.post_detail, name='post_detail'),      # 새로 추가한 URL 패턴), <int:post_id> 부분은 URL 패턴에서 변수를 캡처하는 부분
    path('community/write/', views.post_write, name='post_write'), 
    path('community/post_edit/<int:post_id>/', views.post_edit, name='post_edit'),     # post_edit 수정 부분
    path('community/post_delete/<int:post_id>/',views.post_delete, name="post_delete"),

    path('community/post/<int:post_id>/add_comment/', views.add_comment, name='add_comment'),
    path('community/post/<int:post_id>/like/', views.post_like, name='post_like'),            #추천 비추천
    path('community/post/<int:post_id>/dislike/', views.post_dislike, name='post_dislike'),
    path("community/search/", views.post_search, name="post_search"),

    
    #챔피언 티어 및 로테이션 정보
    path('champions/', views.champions, name='champions'),
    path('champions/champions_tier/<str:position>/<str:region>/<str:tier>', views.champion_tier_list, name='champion_tier'),
    path('champions/lotation/', views.lotation_list, name='lotation'),
    path('champions/statistics_champions/<str:position>/<str:region>/<str:tier>/<str:period>/<str:mode>', views.statistics_champions_list, name='statistics_champions'),

    #인게임 정보
    path('ingame/', views.ingame, name='ingame'),
    path('ingame/<str:nickname>', views.ingame_info, name='ingame_info'),
    
    # 전적 검색
    path('summoners_form', views.summoners_info_form, name='summoners_info_form'),
    path('summoners/<str:country>/<str:summoner_name>', views.summoners_info, name='summoners_info'),   #검색결과를 보여줄 화면
    path('api/summoners_info/<str:country>/<str:summoner_name>/<int:count>/<int:queue>', views.summoners_info_api, name='summoners_info_api'),
]
