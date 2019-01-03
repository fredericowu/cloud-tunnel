from django.contrib.auth.models import User, Group
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings

@receiver(post_save, sender=User)
def post_save_user_set_is_staff(sender, instance, created, **kwargs):
    if created:
        instance.is_staff = True
        group = Group.objects.get(name=settings.DEFAULT_GROUP_NAME)
        instance.groups.add(group)
        instance.save()

