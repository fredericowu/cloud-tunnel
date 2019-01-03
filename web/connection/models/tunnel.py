from django.db import models
from django.utils.translation import ugettext as _
from django.conf import settings
from django.utils import timezone
from .client import Client


class Tunnel(models.Model):
    name = models.CharField(max_length=150)
    endpoint_ip = models.CharField(max_length=15, null=True, blank=True, default=None)
    bind_address = models.CharField(max_length=15, null=True, blank=True, default=None)
    bind_port = models.CharField(max_length=5, null=True, blank=True, default=None)
    creation = models.DateField(auto_now_add=True)
    authorized_access = models.TextField(null=True, blank=True, default=None)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=True,
        default=None,
        null=True,
        related_name="tunnel"
    )

    def __str__(self):
        return self.name

    @classmethod
    def get_free_address_and_port(cls):
        return '0.0.0.0', 5050

    def save(self, *args, **kwargs):
        self.bind_address, self.bind_port = self.get_free_address_and_port()
        if not self.authorized_access:
            self.authorized_access = '*.*.*.*'
        super().save(*args, **kwargs)



