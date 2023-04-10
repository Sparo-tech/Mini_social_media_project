from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView
from .models import UserPostModel
from profiles.models import Profile
from django.http import JsonResponse
from .forms import UserPostEditForm,UserPostForm
from django.contrib.auth.models import User
from itertools import chain
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required()
def HomeView(request):
     # goal is to get post of the logged in user and post of the users the logged in user is following
    form=UserPostForm()
  
    
    # get all post belonging to the logged in user
    request_user_posts = UserPostModel.objects.filter(user=request.user)
    
    # append the logged in users post to a list called logged_in_user_posts.
    logged_in_user_posts = [x for x in request_user_posts]
    
        
    # get logged in user followed profiles
    followed_profiles = Profile.objects.get(user=request.user).all_following()
    
    all_posts=[]
    combined_query =[]
    for profile in followed_profiles:
        # get user object that matches profile
        user_profile = User.objects.get(username = profile.username)

        # get the posts that belongs to each of these users
        followed_feed = UserPostModel.objects.filter(user=user_profile)
        
            
        combined_query.extend(followed_feed)
        
        all_posts = chain(combined_query,logged_in_user_posts)
        reversed_chain = chain(reversed(list(all_posts)))
        
   
    return render(request,'posts/index.html',{'object_list':reversed_chain,'form':form})






@login_required
def PostView(request):
    form = UserPostForm()
    if request.method == 'POST':
            form = UserPostForm(request.POST or None,request.FILES or None)
            if form.is_valid():
                form.save()
                return redirect('posts:home')
    return render(request,'posts/post-content.html',{'form':form})


@login_required
def edit_view(request,pk):
    post = UserPostModel.objects.get(pk=pk)
    form = UserPostEditForm(instance=post)
    if request.method == 'POST':
        form = UserPostEditForm(request.POST or None,request.FILES or None,instance=post)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return redirect('/edit'+'/'+'{}'.format(pk))

    return render(request,'posts/edit-posts.html',{'form':form,'post':post})

@login_required(login_url ='users:login')
def delete_view(request):
    if request.method == 'POST':
        pk = request.POST.get('post_id')
        post = get_object_or_404(UserPostModel,pk=pk)
        post.delete()
        return redirect('/')


@login_required
def like_view(request):
    if request.method=='POST':
        pk = request.POST.get('post_id')
        post = get_object_or_404(UserPostModel,pk=pk)
        liked=False
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            return redirect('/')
        else:
            post.likes.add(request.user)
        return redirect('/')
    else:
        return redirect('/')

    


    




