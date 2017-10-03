from django import forms
from .models import Anouncements
from .models import Soclist
from .models import Faq
from .models import Events
from .models import Achievements
from .models import Contact


class AnouncementsForm(forms.ModelForm):
    class Meta:
        model = Anouncements
        fields = ('soc_no', 'title',)


class SoclistForm(forms.ModelForm):
    class Meta:
        model = Soclist
        fields = ('name', 'email','genre', 'typ', 'logo', 'desc')


class FaqForm(forms.ModelForm):
    class Meta:
        model = Faq
        fields = ('soc_no', 'tag', 'ques', 'ans')



class EventsForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ('soc_no', 'name', 'sdate', 'edate', 'image', 'place', 'desc')



class AchievementsForm(forms.ModelForm):
    class Meta:
        model = Achievements
        fields = ('soc_no', 'title', 'image', 'desc')



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('soc_no', 'ph_no', 'fb', 'twitter', 'insta')


