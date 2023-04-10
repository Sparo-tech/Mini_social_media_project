from django.contrib import admin
from django.urls import path
from .views import CommentView

app_name='Comment'

urlpatterns = [
    path('',CommentView,name='post-comment')
]

