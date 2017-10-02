<<<<<<< HEAD
from django.conf.urls import url
from . import views


urlpatterns=[
    url(r'^userprofile/$',views.Profile_homeList.as_view(),name='profile_home'),
=======
from django.conf.urls import url
from . import views


urlpatterns=[
    url(r'^userprofile/$',views.Profile_homeList.as_view(),name='profile_home'),
>>>>>>> 26ea2e7b37ada947e854bed8410820022a930e73
]