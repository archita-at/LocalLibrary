from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import *

@receiver(post_save, sender=Profile)
def build_profile_on_user_creation(sender, instance, created, **kwargs):
  if created:
    profile = Profile(user=instance)
    profile.save()
  else:
      Profile.objects.create_user(user=instance)