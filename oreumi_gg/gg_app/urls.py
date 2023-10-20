from django.urls import path
from . import views
# from django.conf import settings
# from django.conf.urls.static import static
 
app_name = 'gg_app'    #score 어플리케이션의 url 호출시 앞의 구분자 사용을 하시려면 작성합시다.
 
urlpatterns = [
    path('', views.index, name='index'),
    path('post/', views.post, name='post'),
    path('create/', views.post_create, name='post_create'),                  # create. post 원리 이해하기
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),      # 새로 추가한 URL 패턴), <int:post_id> 부분은 URL 패턴에서 변수를 캡처하는 부분
    path('post_edit/<int:post_id>/', views.post_edit, name='post_edit'),     # post_edit 수정 부분

]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)