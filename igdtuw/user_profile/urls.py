from django.conf.urls import url
from . import views
from user_profile.views import Profile_homeList



urlpatterns=[
    url(r'^profile_home/add/$', views.profile_home_add, name='profile_home_add'),
    url(r'^profile_home/$',views.Profile_homeList.as_view(),name='profile_homelist'),
    url(r'$',views.home, name='home'),
]