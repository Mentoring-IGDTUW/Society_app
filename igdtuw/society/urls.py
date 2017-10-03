from django.conf.urls import url
from . import views
from society.views import SoclistList
from society.views import AnouncementsList
from society.views import EventsList
from society.views import FaqList
from society.views import ContactList
from society.views import AchievementsList




urlpatterns=[
    url(r'^soclist/add/$', views.soclist_add, name='soclist_add'),
    url(r'^soclist/$',SoclistList.as_view(),name='soclistlist'),
    url(r'^anouncements/add/$', views.anouncements_add, name='anouncements_add'),
    url(r'^anouncements/$',AnouncementsList.as_view(),name='anouncementslist'),
    url(r'^events/add/$', views.events_add, name='events_add'),
    url(r'^events/$',EventsList.as_view(),name='eventslist'),
    url(r'^faq/add/$', views.faq_add, name='faq_add'),
    url(r'^faq/$',FaqList.as_view(),name='faqlist'),
    url(r'^contact/add/$', views.contact_add, name='contact_add'),
    url(r'^contact/$',ContactList.as_view(), name='contactlist'),
    url(r'^achievements/add/$', views.achievements_add, name='achievements_add'),
    url(r'^achievements/$',AchievementsList.as_view(),name='achievementslist'),
    url(r'$',views.index, name='index'),


]