from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Shorts


@receiver(post_save, sender=Shorts)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()