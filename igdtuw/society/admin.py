<<<<<<< HEAD
from django.contrib import admin
from .models import Soclist,Events,Faq,Contact,Achievements,Anouncements
# Register your models here.
admin.site.register(Soclist)
admin.site.register(Events)
admin.site.register(Contact)
admin.site.register(Faq)
admin.site.register(Achievements)
=======
from django.contrib import admin
from .models import Soclist,Events,Contact,Faq,Achievements,Anouncements
# Register your models here.
admin.site.register(Soclist)
admin.site.register(Events)
admin.site.register(Contact)
admin.site.register(Faq)
admin.site.register(Achievements)
>>>>>>> 26ea2e7b37ada947e854bed8410820022a930e73
admin.site.register(Anouncements)