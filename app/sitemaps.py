from django.contrib.sitemaps import Sitemap
from .models import Jokes, Memes, Shorts, Stories

class JokesSitemap(Sitemap):
    changefreq = 'daily'
    priority = 1.0

    def items(self):
        return Jokes.objects.all()

class MemesSitemap(Sitemap):
    changefreq = 'daily'
    priority = 1.0

    def items(self):
        return Memes.objects.all()

class ShortsSitemap(Sitemap):
    changefreq = 'daily'
    priority = 1.0

    def items(self):
        return Shorts.objects.all()

