from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404
from .models import STATUS, DarkJokes, Jokes, Memes, Shorts, Stories, LikePost,StripeCustomer
from .forms import RegisterForm
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserUpdateForm, StoryForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from verify_email.email_handler import send_verification_email
from django.conf import settings
from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
def index(request):
    jokes = Jokes.objects.all()[:5]
    context = {
        'jokes':jokes
    }

    return render(request, 'index.html', context = context)

@login_required
def home(request):
    jokes = Jokes.objects.all()[5:15]
    dark_jokes = DarkJokes.objects.all()[:10]
    context = {
        'jokes':jokes,
        'dark_jokes':dark_jokes
    }

    return render(request, 'home.html', context = context)

def meme(request):
    memes = Memes.objects.all()[:10]
    context = {
        'memes':memes
    }
    return render(request, 'memes.html', context=context)

def shorts(request):
    shorts = Shorts.objects.all()[:10]
    context = {
        'shorts':shorts
    }
    return render(request, 'shorts.html', context=context)

class StoryListView(generic.ListView):
    queryset = Stories.objects.filter(status=1).order_by('-created_on')


def stories(request):
    stories = Stories.objects.filter(status=1).order_by('-created_on')
    context = {
        'stories':stories,
    } 
    return render(request, 'stories.html', context=context)


def story_upload(request):
    form = StoryForm(request.POST or None, request.FILES or None)
    if request.method =='POST':
          
        if form.is_valid():
              
            obj = form.save(commit = False)
            obj.user = request.user
            obj.save()
            messages.success(request, "Successfully created")
            return redirect('stories')
        else:
            form = StoryForm()
            
            
          
  
    return render(request, 'earn.html', {'form':form})

    
def LikeView(request):
    story = get_object_or_404(Stories, id=request.POST.get('story_id'))
   
    if story.likes.filter(id=request.user.id).exists():
        story.likes.remove(request.user)
    else:
        story.likes.add(request.user)


        

    return HttpResponseRedirect(reverse('stories'))


def LikeMeme(request):
    meme = get_object_or_404(Memes, id=request.POST.get('meme_id'))

    if meme.likes.filter(id=request.user.id).exists():
        meme.likes.remove(request.user)
    else:
        meme.likes.add(request.user)
    
    return HttpResponseRedirect(reverse('memes'))


def LikeWhite(request):
    joke = get_object_or_404(Jokes, id=request.POST.get('joke_id'))
   
    if joke.likes.filter(id=request.user.id).exists():
        joke.likes.remove(request.user)
    else:
        joke.likes.add(request.user)


        

    return HttpResponseRedirect(reverse('home'))


def LikeDark(request):
    dark = get_object_or_404(DarkJokes, id=request.POST.get('dark_joke_id'))
   
    if dark.likes.filter(id=request.user.id).exists():
        dark.likes.remove(request.user)
    else:
        dark.likes.add(request.user)


        

    return HttpResponseRedirect(reverse('home'))

def LikeShort(request):
    short = get_object_or_404(Shorts, id=request.POST.get('short_id'))
   
    if short.likes.filter(id=request.user.id).exists():
        short.likes.remove(request.user)
    else:
        short.likes.add(request.user)


        

    return HttpResponseRedirect(reverse('shorts'))

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            inactive_user = send_verification_email(request, form)
            messages.success(request, 'We have sent an account activation link to your email. Please check your inbox or spam')
            #form.save()
            return redirect('register')
        return render(request, "register.html", {"form":form})
    else:
        form = RegisterForm()

        return render(request, "register.html", {"form":form})

def profile(request, username):
    if request.method == 'POST':
        user = request.user
        form = UserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user_form = form.save()

            messages.success(request, f'{user_form}, Your profile has been updated!')
            return redirect('profile', user_form.username)

        for error in list(form.errors.values()):
            messages.error(request, error)

    user = User.objects.filter(username=username).first()
    user_stories = Stories.objects.filter(user__exact = user.id)
    if user:
        form = UserUpdateForm(instance=user)
        return render(request, 'accounts.html', context={'form': form, 'stories':user_stories})

    return redirect('home')
