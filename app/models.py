from distutils.command.upload import upload
from email.mime import image
from email.policy import default
from time import timezone
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip
from django.conf import settings
import os
import uuid

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Jokes(models.Model):
    joke = models.TextField(help_text='Enter a joke')
    likes = models.ManyToManyField(User, related_name='like_joke', default=None, blank=True)
    like_count = models.BigIntegerField(default='0')
 
    category= models.ForeignKey(Category,on_delete=models.CASCADE,default=1 )
    

    def __str__(self):
        return self.joke
    
    def get_absolute_url(self):
        return reverse('home')

class Memes(models.Model):
    name = models.CharField(max_length=50, help_text="upload a meme")
    image = models.ImageField(upload_to = 'memes', blank=False, default='memes/download.jpg')
    category= models.ForeignKey(Category,on_delete=models.CASCADE,blank=False, default=1 )
    likes = models.ManyToManyField(User, related_name='like', default=None, blank=True)
    like_count = models.BigIntegerField(default='0')

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('memes')
    
    @property
    def absolute_meme_url(self):
        base_url = 'http://127.0.0.1:8000'
        return f"{base_url}{self.image.url}"
    
class DarkJokes(models.Model):
    dark_joke = models.TextField(help_text='Enter a dark joke')
    likes = models.ManyToManyField(User, related_name='like_dark', default=None, blank=True)
    like_count = models.BigIntegerField(default='0')

    category= models.ForeignKey(Category,on_delete=models.CASCADE,default=1 )

    def __str__(self):
        return self.dark_joke
    def get_absolute_url(self):
        return reverse('home')

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
    image = models.ImageField(upload_to = 'memes', blank=False, default='memes/download.jpg')
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


class Shorts(models.Model):
    name = models.CharField(max_length=50, help_text="upload a short")
    video = models.FileField(upload_to='shorts', blank=False, default='shorts/download.mp4')
    thumbnail = models.ImageField(upload_to='shorts/thumbnails', blank=True, default='shorts/thumbnails/download.jpg')
    source = models.CharField(max_length=255, default='#', blank=True)
    likes = models.ManyToManyField(User, related_name='like_short', default=None, blank=True)
    like_count = models.BigIntegerField(default='0')

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('shorts')
    
    @property
    def absolute_video_url(self):
        base_url = 'http://127.0.0.1:8000'
        return f"{base_url}{self.video.url}"

    def save(self, *args, **kwargs):
        if not self.pk:  # Only cut video if this is a new instance (i.e., the video has not been cut before)
            super().save(*args, **kwargs)  # Save the instance first to get a valid primary key

            # Cut video into a subclip and store it using python moviepy
            input_video = VideoFileClip(self.video.path)
            sep = os.path.sep
            filename, ext = os.path.splitext(os.path.basename(self.video.name))
            new_filename = f'{filename}_{uuid.uuid4()}{ext}'
            new_path = os.path.join(settings.MEDIA_ROOT, 'shorts', new_filename)
            end_time = input_video.duration - 4
            ffmpeg_extract_subclip(self.video.path, 0, end_time, targetname=new_path)

            # Update the video field with the new path
            self.video.name = os.path.relpath(new_path, settings.MEDIA_ROOT)
            input_video.close()
        super().save(*args, **kwargs)  # Save the instance with the updated video path

        

class LikePost(models.Model):
    story = models.ForeignKey(Stories,on_delete=models.CASCADE, null=True)
    short = models.ForeignKey(Shorts,on_delete=models.CASCADE, null=True)
    meme = models.ForeignKey(Memes,on_delete=models.CASCADE, null=True)
    joke = models.ForeignKey(Jokes,on_delete=models.CASCADE, null=True)
    dark_joke = models.ForeignKey(DarkJokes,on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)


class StripeCustomer(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    stripeCustomerId = models.CharField(max_length=255)
    stripeSubscriptionId = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username



        




# Create your models here.
