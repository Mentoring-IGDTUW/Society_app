<<<<<<< HEAD
from django.db import models

class Soclist(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    genre=models.CharField(max_length=50)
    typ=models.CharField(max_length=50)
    logo=models.CharField(max_length=250)
    desc=models.TextField(max_length=500)

    def __str__(self):
        return self.name

class Anouncements(models.Model):
    soc_no=models.ForeignKey(Soclist,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Events(models.Model):
    soc_no=models.ForeignKey(Anouncements,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    sdate=models.DateTimeField()
    edate=models.DateTimeField()
    image=models.CharField(max_length=250)
    place=models.CharField(max_length=100)
    desc=models.TextField(max_length=500)

    def __str__(self):
        return self.name

class Contact(models.Model):
    soc_no=models.ForeignKey(Soclist,on_delete=models.CASCADE)
    ph_no=models.BigIntegerField()
    fb=models.CharField(max_length=250)
    twitter=models.CharField(max_length=250)
    insta=models.CharField(max_length=250)

    def __str__(self):
        return self.fb

class Faq(models.Model):
    soc_no=models.ForeignKey(Soclist,on_delete=models.CASCADE)
    tag=models.CharField(max_length=100)
    ques=models.CharField(max_length=200)
    ans=models.TextField(max_length=500)

    def __str__(self):
        return self.tag

class Achievements(models.Model):
    soc_no=models.ForeignKey(Soclist,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    image=models.CharField(max_length=250)
    desc=models.TextField(max_length=500)

    def __str__(self):
        return self.title

=======
from django.db import models

class Soclist(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    genre=models.CharField(max_length=50)
    typ=models.CharField(max_length=50)
    logo=models.CharField(max_length=250)
    desc=models.TextField(max_length=500)

    def __str__(self):
        return self.name

class Anouncements(models.Model):
    soc_no=models.ForeignKey(Soclist,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Events(models.Model):
    soc_no=models.ForeignKey(Anouncements,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    sdate=models.DateTimeField()
    edate=models.DateTimeField()
    image=models.CharField(max_length=250)
    place=models.CharField(max_length=100)
    desc=models.TextField(max_length=500)

    def __str__(self):
        return self.name

class Contact(models.Model):
    soc_no=models.ForeignKey(Soclist,on_delete=models.CASCADE)
    ph_no=models.BigIntegerField()
    fb=models.CharField(max_length=250)
    twitter=models.CharField(max_length=250)
    insta=models.CharField(max_length=250)

    def __str__(self):
        return self.fb

class Faq(models.Model):
    soc_no=models.ForeignKey(Soclist,on_delete=models.CASCADE)
    tag=models.CharField(max_length=100)
    ques=models.CharField(max_length=200)
    ans=models.TextField(max_length=500)

    def __str__(self):
        return self.tag

class Achievements(models.Model):
    soc_no=models.ForeignKey(Soclist,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    image=models.CharField(max_length=250)
    desc=models.TextField(max_length=500)

    def __str__(self):
        return self.title

>>>>>>> 26ea2e7b37ada947e854bed8410820022a930e73
