from django.http import HttpResponse
from society.models import Soclist
from society.models import Anouncements
from society.models import Events
from society.models import Faq
from society.models import Contact
from society.models import Achievements
from .forms import EventsForm
from .forms import SoclistForm
from .forms import FaqForm
from .forms import ContactForm
from .forms import AchievementsForm
from .forms import AnouncementsForm

from django.shortcuts import redirect,render
from django.template import loader




from django.views.generic import ListView

# Create your views here.
def index(request):

    all_anouncements=Anouncements.objects.all()
    all_soclist = Soclist.objects.all()
    all_faq = Faq.objects.all()
    all_events = Events.objects.all()
    all_contact = Contact.objects.all()
    all_achievements = Achievements.objects.all()
    template = loader.get_template('society/base.html')
    context={
        'all_soclist':  all_soclist,
        'all_faq':all_faq,
        'all_events':all_events,
        'all_contact':all_contact,
        'all_achievements':all_achievements,
        'all_anouncements':all_anouncements,

    }
    return HttpResponse(template.render(context,request))


def anouncements_add(request):

    if request.method == "POST":
        form = AnouncementsForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('society/base', pk=post.pk)
    else:
        form = AnouncementsForm()
    return render(request, 'society/Anouncements_edit.html', {'form': form})


def soclist_add(request):

    if request.method == "POST":
        form = SoclistForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('society/base', pk=post.pk)
    else:
        form = SoclistForm()
    return render(request, 'society/Soclist_edit.html', {'form': form})


def events_add(request):

    if request.method == "POST":
        form = EventsForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('society/base', pk=post.pk)
    else:
        form = EventsForm()
    return render(request, 'society/Events_edit.html', {'form': form})


def contact_add(request):

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('society/base', pk=post.pk)
    else:
        form = ContactForm()
    return render(request, 'society/Contact_edit.html', {'form': form})


def faq_add(request):

    if request.method == "POST":
        form = FaqForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('society/base', pk=post.pk)
    else:
        form = FaqForm()
    return render(request, 'society/Faq_edit.html', {'form': form})


def achievements_add(request):

    if request.method == "POST":
        form = AchievementsForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('society/base', pk=post.pk)
    else:
        form = AchievementsForm()
    return render(request, 'society/Achievements_edit.html', {'form': form})





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
    model = Achievements