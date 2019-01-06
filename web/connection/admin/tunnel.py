from django.contrib import admin
from ..models.tunnel import Tunnel
from common.admin import ModelAdminCommon


class TunnelAdmin (ModelAdminCommon):
    pass


admin.site.register(Tunnel, TunnelAdmin)
