from django.contrib import admin
from core.models import FiscalYear
from core.models import AppSetting

admin.site.register(FiscalYear)


class SettingsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False


admin.site.register(AppSetting, SettingsAdmin)


