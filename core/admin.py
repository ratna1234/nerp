from django.contrib import admin
from core.models import FiscalYear, AppSetting, Donor, Activity, Budget, Employee, Party

admin.site.register(FiscalYear)
admin.site.register(Donor)
admin.site.register(Activity)
admin.site.register(Budget)
admin.site.register(Employee)
admin.site.register(Party)


class SettingsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False


admin.site.register(AppSetting, SettingsAdmin)


