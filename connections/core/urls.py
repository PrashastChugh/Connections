from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('settings', views.settings, name='settings'),                # 10)
    path('upload', views.upload, name='upload'),                      # 11)
    path('follow', views.follow, name='follow'),
    path('search', views.search, name='search'),
    path('profile/<str:pk>', views.profile, name='profile'),                      # 14)
    path('like-post', views.like_post, name='like-post'),             # 13)
    path('signup', views.signup, name='signup'),                      # 8)
    path('signin', views.signin, name='signin'),                      # 9)
    path('logout', views.logout, name='logout'),                      # 9)
]
