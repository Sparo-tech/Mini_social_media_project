from django.contrib import admin
from django.urls import path,include
from .views import ProfileView,EditProfileView,AllProfilesView,DetailProfilesView,follow_unfollow_view

app_name='profiles'

urlpatterns = [
    path('',ProfileView,name='profile-view'),
    path('edit-profile/',EditProfileView,name='edit-profile'),
    path('all-profiles/',AllProfilesView,name='all-profiles'),
    path('profile/<slug>',DetailProfilesView,name='view-another-profile'),
    path('follow/',follow_unfollow_view,name='follow-another-profile'),
]
