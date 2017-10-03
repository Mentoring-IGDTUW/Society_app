from django.http import HttpResponse
from user_profile.models import Profile_home
from django.views.generic import ListView
from .forms import Profile_homeForm
from django.template import loader
from django.shortcuts import redirect,render

# Create your views here.
def home(request):

    all_Profile_home = Profile_home.objects.all()
    template = loader.get_template('user_profile/home.html')
    context={
        'Profile_home' :Profile_home,

    }
    return HttpResponse(template.render(context,request))


def profile_home_add(request):

    if request.method == "POST":
        form = Profile_homeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('user_profile/home', pk=post.pk)
    else:
        form = Profile_homeForm()
    return render(request, 'user_profile/Profile_home_edit.html', {'form': form})



class Profile_homeList(ListView):
    model = Profile_home