from django.db import models
from django.utils.translation import ugettext as _
from django.conf import settings
from django.utils import timezone


class Client(models.Model):
    name = models.CharField(max_length=150)
    client_id = models.CharField(max_length=50, null=True, blank=True, default=None)
    external_ip = models.CharField(max_length=15, null=True, blank=True, default=None)
    internal_ip = models.CharField(max_length=15, null=True, blank=True, default=None)
    gateway = models.CharField(max_length=15, null=True, blank=True, default=None)
    network_mask = models.CharField(max_length=15, null=True, blank=True, default=None)
    authorized = models.BooleanField(default=False)
    last_seen = models.DateField(null=True, blank=True, default=None)
    creation = models.DateField(auto_now_add=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=True,
        default=None,
        null=True,
        related_name="client"
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.name or not self.last_seen:
            if not self.name:
                self.name = "Client-{}".format(self.pk)
            if not self.last_seen:
                self.update_last_seen(save=False)
            self.save()

    def __str__(self):
        return self.name

    def update_last_seen(self, save=True):
        self.last_seen = timezone.now()
        if save:
            self.save()
