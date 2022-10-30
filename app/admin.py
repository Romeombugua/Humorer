from django.contrib import admin
from .models import Category, Jokes, Memes, DarkJokes, Shorts, Stories, StripeCustomer

admin.site.register(Jokes)
admin.site.register(Category)
admin.site.register(Memes)
admin.site.register(DarkJokes)
#admin.site.register(Stories)
admin.site.register(Shorts)
admin.site.register(StripeCustomer)

class StoriesAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']

admin.site.register(Stories, StoriesAdmin)
# Register your models here.
