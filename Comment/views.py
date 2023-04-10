from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import CreateView
from .models import Comment
from  posts.models import UserPostModel
from .models import Comment

# Create your views here.
def CommentView(request):
   
    if request.method == 'POST':
        post_pk = request.POST.get('post_pk')
        comment = request.POST.get('comment')
        post = get_object_or_404(UserPostModel,pk=post_pk)
        if post:
            user_comment = Comment.objects.create(author=request.user,post=post,comment=comment)
            user_comment.save()
        return redirect('/')



