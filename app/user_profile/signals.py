from django.conf import settings
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.db import models 
from django.db.models.signals import post_save
from .models import Profile
from django.contrib.auth.signals import user_logged_in,user_logged_out


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile(sender, instance=None, created=False, **kwargs):
    if created:
        Profile(user=instance,is_online=True).save()







@receiver(user_logged_in, sender=settings.AUTH_USER_MODEL)
def is_online_login(sender, user, request, **kwargs):
    user.profile.is_online = True
    user.profile.save()



@receiver(user_logged_out, sender=settings.AUTH_USER_MODEL)
def is_online_logout(sender, user, request, **kwargs):
    print(user,"--------------------------------------------")
    user.profile.is_online = False
    user.profile.save()


