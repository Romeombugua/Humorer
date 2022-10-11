from distutils.command.upload import upload
from email.mime import image
from email.policy import default
from time import timezone
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Jokes(models.Model):
    joke = models.TextField(help_text='Enter a joke')
 
    category= models.ForeignKey(Category,on_delete=models.CASCADE,default=1 )
    

    def __str__(self):
        return self.joke

class Memes(models.Model):
    name = models.CharField(max_length=50, help_text="upload a meme")
    image = models.ImageField(upload_to = 'https://drive.google.com/drive/folders/1_gO2nfe7th0Xv9waUdtnIK27nC8Livmy?usp=sharing', blank=False, default='memes/download.jpg')
    category= models.ForeignKey(Category,on_delete=models.CASCADE,default=1 )

    def __str__(self):
        return self.name

class DarkJokes(models.Model):
    dark_joke = models.TextField(help_text='Enter a dark joke')

    category= models.ForeignKey(Category,on_delete=models.CASCADE,default=1 )

    def __str__(self):
        return self.dark_joke

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Stories(models.Model):
    user = models.ForeignKey(User,
                        default = 1,
                        null = True, 
                        on_delete = models.SET_NULL
                        )
    title = models.CharField(max_length = 100)
    image = models.ImageField(upload_to = 'uploads/memes', blank=False, default='memes/download.jpg')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='story_posts')

    class Meta:
        ordering = ['-created_on']
    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('stories', kwargs={'pk': self.pk})

class LikePost(models.Model):
    story = models.ForeignKey(Stories,on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)

class Shorts(models.Model):
    name = models.CharField(max_length=50, help_text="upload a short")
    video = models.CharField(max_length=1000 ,blank=False)
    def __str__(self):
        return self.name

        




# Create your models here.
