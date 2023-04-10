from django.forms import ModelForm
from .models import UserPostModel

class UserPostEditForm(ModelForm):
       
    class Meta:
        model = UserPostModel
        fields=('text','image')


class UserPostForm(ModelForm):
       
    class Meta:
        model = UserPostModel
        fields= ('user','text','image','profile',)





