<<<<<<< HEAD
from django.conf.urls import url
from . import views
from society.views import SoclistList
from society.views import AnouncementsList
from society.views import EventsList
from society.views import FaqList
from society.views import ContactList
from society.views import AchievementsList




urlpatterns=[

    url(r'^soclist/$',SoclistList.as_view()),
    url(r'^anouncements/$',AnouncementsList.as_view()),
    url(r'^events/$',EventsList.as_view()),
    url(r'^faq/$',FaqList.as_view()),
    url(r'^contact/$',ContactList.as_view()),
    url(r'^achievements/$',AchievementsList.as_view()),



=======
from django.conf.urls import url
from . import views
from society.views import SoclistList
from society.views import AnouncementsList
from society.views import EventsList
from society.views import FaqList
from society.views import ContactList
from society.views import AchievementsList




urlpatterns=[

    url(r'^soclist/$',SoclistList.as_view()),
    url(r'^anouncements/$',AnouncementsList.as_view()),
    url(r'^events/$',EventsList.as_view()),
    url(r'^faq/$',FaqList.as_view()),
    url(r'^contact/$',ContactList.as_view()),
    url(r'^achievements/$',AchievementsList.as_view()),



>>>>>>> 26ea2e7b37ada947e854bed8410820022a930e73
]