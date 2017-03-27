from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

#defining post as an object, models.Model --> django weet dit in db moet
class Post(models.Model):
    #Properties definen met de juiste fieldtype
    #voor all field type check: 
    #https://docs.djangoproject.com/en/1.10/ref/models/fields/#field-types

    #link naar een ander model
    author = models.ForeignKey('auth.User')
    #CharField voor tekst met limiet
    title = models.CharField(max_length=200)
    #TextField voor tekst zonder limiet
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    #LET OP!! True en False ALTIJD BEGINNEN MET HOOFDLETTERS GEVOLGD DOOR KLEINE
    published_date = models.DateTimeField(blank=True, null=True)

    #methodes name convention: Underscores!! no CC
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title