from django.conf.urls import patterns, include, url
from django.contrib import admin

from users import views as users_views

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       url(r'^$', users_views.index, name='home'),
                       (r'^user/', include('users.urls')),
                       # url(r'^app/', include('app.foo.urls')),

                       (r'^inventory/', include('inventory.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^settings/', include('livesettings.urls')),
                       (r'^i18n/', include('django.conf.urls.i18n')),


)
