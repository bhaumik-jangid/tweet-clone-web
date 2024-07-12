from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.urls import reverse
from .forms import TweetForm, UserRegisterationForm, CustomAuthenticationForm, CustomEditProfileForm
from .models import Tweet, TweetUserData
from django.db.models import Count, Q 

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    form_class = CustomAuthenticationForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            form.save()
            login(request, user)
            return redirect('edit_profile', username=user.username)
    else:
        form = UserRegisterationForm()
    return render(request,'registration/register.html', {'form': form})
    
def UserLogin(request):
    form = UserRegisterationForm(request.POST or None)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('tweet_list')
    return render(request,'registration/login.html', {'form': form})

def home(request):
    return redirect('tweet_list')

def tweet_list(request):
    tweets = Tweet.objects.select_related('user__tweetuserdata').all().order_by('-created_at')
    return render(request, 'tweet_list.html', {'tweets': tweets})

@login_required
def create_tweet(request):
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('tweet_list')
    else:
        form = TweetForm()
    
    user_profile_data = get_object_or_404(TweetUserData, user=request.user)
    return render(request,'create_tweet.html', {'form': form, 'user_profile_data': user_profile_data})

@login_required
def edit_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('tweet_list')
    else:
        form = TweetForm(instance=tweet)
    user_profile_data = get_object_or_404(TweetUserData, user=request.user)
    return render(request,'create_tweet.html', {'form': form, 'tweet': tweet, 'user_profile_data': user_profile_data})

@login_required
def delete_tweet(request, tweet_id):
    if request.method == 'POST':
        tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
        tweet.delete()
        return redirect('tweet_list')
    return render(request,'tweet_delete_confirm.html')

@login_required
def notification(request):
    return render(request,'notification.html')

def search_user(request):
    query = request.GET.get('query', '')
    if query:
        user_datas = TweetUserData.objects.select_related('user').filter(
            Q(first_name__icontains=query) | 
            Q(last_name__icontains=query) |
            Q(user__username__icontains=query)
        ).order_by('-user__last_login')
    else:
        user_datas = TweetUserData.objects.select_related('user').order_by('-user__last_login')

    return render(request, 'search/search_user.html', {'user_datas': user_datas})

def search_tweets(request):
    query = request.GET.get('query')
    
    if query:
        tweets = Tweet.objects.filter(
            Q(text__icontains=query)
        ).select_related('user').order_by('-updated_at')
    else:
        tweets = Tweet.objects.select_related('user').order_by('-updated_at')

    return render(request, 'search/search_tweets.html', {'tweets': tweets})

def profile(request, username):
    user = get_object_or_404(User, username=username)
    tweet_user_data, created = TweetUserData.objects.get_or_create(user=user)
    tweets = Tweet.objects.filter(user=user).order_by('-created_at')
    return render(request, 'profile.html', {'tweets': tweets, 'profileData': tweet_user_data})

@login_required
def edit_profile(request, username):
    user = request.user
    tweet_user_data, created = TweetUserData.objects.get_or_create(user=user)

    if request.method == 'POST':
        form = CustomEditProfileForm(request.POST, request.FILES, instance=tweet_user_data)
        if form.is_valid():
            form.save()
            return redirect(reverse('profile', kwargs={'username': user.username}))
    else:
        form = CustomEditProfileForm(instance=tweet_user_data)
    
    return render(request, 'edit_profile.html', {'form': form})

def delete_user(request, username):
    user = get_object_or_404(User, username=username)
    if request.method == 'POST':
        user.delete()
        return redirect('home')
    return render(request, 'confirmation.html')