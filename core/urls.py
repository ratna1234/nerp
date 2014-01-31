from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',

                       url(r'^parties/$', views.list_parties, name='list_parties'),
                       url(r'^party/create/$', views.party_form, name='create_party'),
                       url(r'^party/(?P<id>[0-9]+)/delete/$', views.delete_party, name='delete_party'),
                       url(r'^party/(?P<id>[0-9]+)/$', views.party_form, name='update_party'),
                       url(r'^parties.json$', views.parties_as_json, name='parties_as_json'),

)