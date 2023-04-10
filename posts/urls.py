from django.contrib import admin
from django.urls import path,include
from .views import HomeView,like_view,edit_view,delete_view,PostView
app_name='posts'

urlpatterns = [
    path('',HomeView,name='home'),
     path('edit/<int:pk>',edit_view,name='edit-post'),
     path('delete/',delete_view,name='delete-post'),
    path('like/',like_view,name='like-view'),
    path('post/',PostView,name='post-view')
]
