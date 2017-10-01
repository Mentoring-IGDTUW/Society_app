from django.db import models

# Create your models here.
class Profile_home(models.Model):
    name=models.CharField(max_length=50)
    en_no=models.BigIntegerField(primary_key=True)
    year=models.IntegerField()
    branch=models.CharField(max_length=100)
    email=models.EmailField()
    ph_no=models.BigIntegerField()
    password=models.CharField(max_length=50)
    profile_pic=models.CharField(max_length=250)

    def __str__(self):
        return self.name+'-'+str(self.en_no)
