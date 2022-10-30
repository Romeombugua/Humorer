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
import stripe
def index(request):
    jokes = Jokes.objects.all()[:5]
    context = {
        'jokes':jokes
    }

    return render(request, 'index.html', context = context)

@login_required
def home(request):
    jokes = Jokes.objects.all()[:10]
    dark_jokes = DarkJokes.objects.all()
    context = {
        'jokes':jokes,
        'dark_jokes':dark_jokes
    }

    return render(request, 'home.html', context = context)

def meme(request):
    memes = Memes.objects.all()
    context = {
        'memes':memes
    }
    return render(request, 'memes.html', context=context)

def shorts(request):
    shorts = Shorts.objects.all()
    context = {
        'shorts':shorts
    }
    return render(request, 'shorts.html', context=context)

'''def StoryDetail(request):
    story = Stories.objects.filter(status=1).order_by('-created_on')
    provider = get_object_or_404(Stories,id=request.POST.get('story_id'))
    total_likes = provider.total_likes()
    context = {
        'story':story,
        'total_likes':total_likes
    }
    return render(request, '/app/stories_detail.html', context=context)
'''

class StoryListView(generic.ListView):
    queryset = Stories.objects.filter(status=1).order_by('-created_on')

    '''def get_context_data(self,*args, **kwargs):
        context = super(StoryListView,self).get_context_data(*args,**kwargs)
        provider = get_object_or_404(Stories, id=self.kwargs.get('pk'))
        total_likes = provider.total_likes()
        context['total_likes'] = total_likes
        return context
        '''
def stories(request):
    try:
        # Retrieve the subscription & product
        stories = Stories.objects.filter(status=1).order_by('-created_on')
        stripe_customer = StripeCustomer.objects.get(user=request.user)
        stripe.api_key = settings.STRIPE_SECRET_KEY
        subscription = stripe.Subscription.retrieve(stripe_customer.stripeSubscriptionId)
        #product = stripe.Product.retrieve(subscription.plan.product)

        # Feel free to fetch any additional data from 'subscription' or 'product'
        # https://stripe.com/docs/api/subscriptions/object
        # https://stripe.com/docs/api/products/object

        return render(request, 'stories.html', {
            'stories':stories,
            'subscription': subscription,
        })

    except StripeCustomer.DoesNotExist:
        return render(request, 'subscribe.html')


'''def stories(request):
    stories = Stories.objects.filter(status=1).order_by('-created_on')
    stripe_customer = StripeCustomer.objects.get(user=request.user)
    stripe.api_key = settings.STRIPE_SECRET_KEY
    subscription = stripe.Subscription.retrieve(stripe_customer.stripeSubscriptionId)
    context = {
        'stories':stories,
        'subscription':subscription,
    } 
    return render(request, 'stories.html', context=context)'''


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

'''def LikeView(request):
    user_id = request.user.id
    story_id = request.POST.get('story_id')
    story = Stories.objects.get(id=story_id)

    like_filter = LikePost.objects.filter(story_id=story_id,user_id=user_id).first()

    if like_filter == None:
        new_like = LikePost.objects.create(story_id=story_id, user_id=user_id)
        new_like.save()
        story.likes = story.likes+1
        story.save()
        return HttpResponseRedirect(reverse('stories'))
    else:
        like_filter.delete()
        story.likes = story.likes-1
        story.save()
        return HttpResponseRedirect(reverse('stories'))'''



def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            inactive_user = send_verification_email(request, form)
            #form.save()
            return redirect('home')
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

@login_required
def subscribe(request):
    try:
        # Retrieve the subscription & product
        stripe_customer = StripeCustomer.objects.get(user=request.user)
        stripe.api_key = settings.STRIPE_SECRET_KEY
        subscription = stripe.Subscription.retrieve(stripe_customer.stripeSubscriptionId)
        product = stripe.Product.retrieve(subscription.plan.product)

        # Feel free to fetch any additional data from 'subscription' or 'product'
        # https://stripe.com/docs/api/subscriptions/object
        # https://stripe.com/docs/api/products/object

        return render(request, 'subscribe.html', {
            'subscription': subscription,
            'product': product,
        })

    except StripeCustomer.DoesNotExist:
        return render(request, 'subscribe.html')


@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)

@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET':
        domain_url = 'http://localhost:8000/app/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            checkout_session = stripe.checkout.Session.create(
                client_reference_id=request.user.id if request.user.is_authenticated else None,
                success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'cancel/',
                payment_method_types=['card'],
                mode='subscription',
                line_items=[
                    {
                        'price': settings.STRIPE_PRICE_ID,
                        'quantity': 1,
                    }
                ]
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})


@login_required
def success(request):
    return render(request, 'success.html')


@login_required
def cancel(request):
    if request.user.is_authenticated:
        sub_id = request.user.subscription.id

        stripe.api_key = settings.STRIPE_SECRET_KEY

        try:
            stripe.Subscription.delete(sub_id)
        except Exception as e:
            return JsonResponse({'error': (e.args[0])}, status =403)
    return render(request, 'cancel.html')

@csrf_exempt
def stripe_webhook(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    endpoint_secret = settings.STRIPE_ENDPOINT_SECRET
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']

        # Fetch all the required data from session
        client_reference_id = session.get('client_reference_id')
        stripe_customer_id = session.get('customer')
        stripe_subscription_id = session.get('subscription')

        # Get the user and create a new StripeCustomer
        user = User.objects.get(id=client_reference_id)
        StripeCustomer.objects.create(
            user=user,
            stripeCustomerId=stripe_customer_id,
            stripeSubscriptionId=stripe_subscription_id,
        )
        print(user.username + ' just subscribed.')

    return HttpResponse(status=200)
# Create your views here.
