from django.conf.urls import url
from . import views


urlpatterns=[
    url(r'^userprofile/$',views.Profile_homeList.as_view(),name='profile_home'),
]