from django.urls import path
from . import views
from django.urls import include
from django.contrib.sitemaps.views import sitemap
from .sitemaps import JokesSitemap, MemesSitemap, ShortsSitemap


sitemaps = {
    'jokes': JokesSitemap,
    'memes': MemesSitemap,
    'shorts': ShortsSitemap,
}


urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.home, name='home'),
    path('jokes', views.joke, name='jokes'),
    path('memes', views.meme, name='memes'),
    path('shorts', views.shorts, name='shorts'),
    #path('stories', views.StoryListView.as_view(), name='stories'),
    path('stories', views.stories, name='stories'),
    path('earn', views.story_upload, name='earn'),
    path('likeDark',views.LikeDark, name='like_dark'),
    path('likeWhite',views.LikeWhite, name='like_white'),
    path('like',views.LikeView, name='like_post'),
    path('likeM',views.like, name='likeM'),
    path('likeShorts',views.LikeShort, name='like_short'),
    #path('<slug:slug>/', views.StoryDetail.as_view(), name='stories_detail'),
    path('register', views.register, name='register'),
    path('profile/<username>', views.profile, name='profile'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    ]