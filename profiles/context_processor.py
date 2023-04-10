from .models import Profile

def profile_pic(request):
    if request.user.is_authenticated:
        profile_obj = Profile.objects.get(user=request.user)
        pic = profile_obj.get_avatar_url
        return {'picture':pic,'user_id':request.user.id}
    return {}