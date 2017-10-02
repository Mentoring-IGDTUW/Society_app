<<<<<<< HEAD
from django.http import HttpResponse
from society.models import Soclist
from society.models import Anouncements
from society.models import Events
from society.models import Faq
from society.models import Contact
from society.models import Achievements



from django.views.generic import ListView

# Create your views here.


class SoclistList(ListView):
    model = Soclist

class AnouncementsList(ListView):
    model = Anouncements

class EventsList(ListView):
    model = Events

class FaqList(ListView):
    model = Faq

class ContactList(ListView):
    model = Contact

class AchievementsList(ListView):
=======
from django.http import HttpResponse
from society.models import Soclist
from society.models import Anouncements
from society.models import Events
from society.models import Faq
from society.models import Contact
from society.models import Achievements



from django.views.generic import ListView

# Create your views here.


class SoclistList(ListView):
    model = Soclist

class AnouncementsList(ListView):
    model = Anouncements

class EventsList(ListView):
    model = Events

class FaqList(ListView):
    model = Faq

class ContactList(ListView):
    model = Contact

class AchievementsList(ListView):
>>>>>>> 26ea2e7b37ada947e854bed8410820022a930e73
    model = Achievements