
"""
import datetime
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here
class Profile(models.Model): #User Profile
    SEX_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('NB', 'Non-binary'),
        ('Z', 'Would rather not say'),
        ('UK', 'Unknown'),)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    sex = models.CharField(max_length=2, choices=SEX_CHOICES,
                           help_text='Select your gender', blank=True, null=True)
    bio = models.TextField(verbose_name="About the Writer", max_length=1000,
                           help_text='Tell your readers about yourself...', blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    city = models.CharField(verbose_name='City', max_length=255,
                            help_text='Where do you live?', blank=True, null=True)
    phone = models.PositiveIntegerField(blank=True, null=True)
    linkedin = models.URLField(verbose_name='LinkedIn', max_length = 200,
                               help_text='Enter your LinkedIn URL here',
                               blank=True, null=True)
    twitter = models.URLField(verbose_name='Twitter', max_length = 200,
                              help_text='Enter your Twitter URL here',
                              blank=True, null=True)
    instagram = models.URLField(verbose_name='Instagram', max_length = 200,
                               help_text='Enter your Instagram URL here', blank=True, null=True)

    #email_confirmed = models.BooleanField(default=False)

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username

    def is_eighteenyrs(self):
        age = datetime.date.today() - self.date_of_birth
        return age >= 18

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

"""