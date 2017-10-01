
from user_profile.models import Profile_home
from django.views.generic import ListView

# Create your views here.
class Profile_homeList(ListView):
    model = Profile_home