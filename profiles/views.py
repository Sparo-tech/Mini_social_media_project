# Create your views here.
from django.shortcuts import render,redirect,get_object_or_404
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def ProfileView(request):
    profile = Profile.objects.get(user=request.user)
    return render(request,'profiles/user-profile.html',{"profile":profile})

@login_required
def EditProfileView(request):
    profile = Profile.objects.get(user=request.user)
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST or None,request.FILES or None,instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profiles:profile-view')
    return render(request,'profiles/edit-profile.html',{"form":form,'profile':profile})

@login_required
def AllProfilesView(request):
    all_profiles= Profile.objects.all().exclude(user=request.user)
    return render(request,'profiles/all-profiles.html',{"all_profiles":all_profiles})

@login_required
def DetailProfilesView(request,slug):
    #to view another user's profile
    profile =Profile.objects.get(slug=slug)
    return render(request,'profiles/another-user-profile.html',{'profile':profile})

@login_required
def follow_unfollow_view(request):
    if request.method == 'POST':
        person_to_follow_or_unfollow_profile_id = request.POST.get('profile_pk')
       
        person_to_unfollow_or_follow_profile = get_object_or_404(Profile,pk=person_to_follow_or_unfollow_profile_id)
        current_user_profile = get_object_or_404(Profile,pk=request.user.id)
        if not current_user_profile.following.filter(id=person_to_follow_or_unfollow_profile_id).exists():
            current_user_profile.following.add(person_to_unfollow_or_follow_profile.user)
            person_to_unfollow_or_follow_profile.followers.add(request.user)
            return redirect('profiles:all-profiles')
        elif current_user_profile.following.filter(id=person_to_follow_or_unfollow_profile_id).exists():
            current_user_profile.following.remove(person_to_unfollow_or_follow_profile.user)
            person_to_unfollow_or_follow_profile.followers.remove(request.user)
            return redirect('profiles:all-profiles')
        return redirect('profiles:all-profiles')
    else:
        return redirect('profiles:all-profiles')

