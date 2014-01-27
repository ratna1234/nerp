from core.models import AppSetting


class SettingMiddleware(object):
    def process_request(self, request):
        app_setting = AppSetting.objects.first()
        request.__class__.setting = app_setting


