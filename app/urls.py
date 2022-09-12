from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('memes', views.meme, name='memes'),
    path('shorts', views.shorts, name='shorts'),
    path('stories', views.StoryListView.as_view(), name='stories'),
    path('earn', views.story_upload, name='earn'),
    path('like',views.LikeView, name='like_post'),
    #path('<slug:slug>/', views.StoryDetail.as_view(), name='stories_detail'),
    path('register', views.register, name='register'),
    path('profile/<username>', views.profile, name='profile'),
    ]