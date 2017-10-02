<<<<<<< HEAD

from user_profile.models import Profile_home
from django.views.generic import ListView

# Create your views here.
class Profile_homeList(ListView):
=======

from user_profile.models import Profile_home
from django.views.generic import ListView

# Create your views here.
class Profile_homeList(ListView):
>>>>>>> 26ea2e7b37ada947e854bed8410820022a930e73
    model = Profile_home