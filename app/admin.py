__author__ = 'xtranophilist'

from django.contrib.admin.sites import AdminSite
from django.utils.module_loading import autodiscover_modules


class CustomAdminSite(AdminSite):
    site_header = 'App Name'


admin_site = CustomAdminSite()