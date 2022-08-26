from django.db import models
from django.contrib.auth.models import User

from django.db import models
from django.forms import IntegerField


# Create your models here.
from django_mysql.models import ListCharField
class Language(models.Model):
    name = models.CharField(max_length=20)
  
    def __str__(self):
        return f"{self.name}"

class Post(models.Model):
    noun= models.IntegerField(blank=True, null=True)
    verb= models.IntegerField(blank=True, null=True)
    article= models.IntegerField(blank=True, null=True)
    adjective= models.IntegerField(blank=True, null=True)
    adverb= models.IntegerField(blank=True, null=True)
    pronoun= models.IntegerField(blank=True, null=True)
    preposition= models.IntegerField(blank=True, null=True)
    sentence=models.IntegerField(blank=True, null=True)
    verbphase=models.IntegerField(blank=True, null=True)
    nounphase=models.IntegerField(blank=True, null=True)
    prepphase=models.IntegerField(blank=True, null=True)
    interjection=models.IntegerField(blank=True, null=True)
    




