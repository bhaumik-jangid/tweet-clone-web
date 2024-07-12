from django.urls import path
from . import views

urlpatterns = [
    path("", views.tweet_list, name='tweet_list'),
    
    # path("login/", views.login, name='login'),
    path('login/', views.CustomLoginView.as_view(), name='UserLogin'),

    path("register/", views.register, name='register'),
    
    path("create_tweet/", views.create_tweet, name='create_tweet'),
    path("<int:tweet_id>/edit_tweet/", views.edit_tweet, name='edit_tweet'),
    path("<int:tweet_id>/delete_tweet/", views.delete_tweet, name='delete_tweet'),
    path("search/user/", views.search_user, name='search_user'),
    path("search/tweets/", views.search_tweets, name='search_tweets'),
    path("notifications/", views.notification, name='notifications'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('edit_profile/<str:username>/', views.edit_profile, name='edit_profile'),
    path('delete_user/<str:username>/', views.delete_user, name='delete_user'),
]