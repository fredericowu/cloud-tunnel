from django.contrib import admin
from .models.client import Client
from common.admin import ModelAdminCommon


class ClientAdmin (ModelAdminCommon):
    readonly_fields = ["last_seen", "network_mask", "gateway", "internal_ip", "external_ip", "client_id", ]


admin.site.register(Client, ClientAdmin)
