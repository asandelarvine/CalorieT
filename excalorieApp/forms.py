from django.forms import ModelForm
from .models import *


class fooditemForm(ModelForm):
    class Meta:
        model=Fooditem
        fields="__all__"

class addUserFooditem(ModelForm):
    class Meta:
        model=UserFooditem
        fields="__all__"
        
class UpdateProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = [ "user"]