from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',

                       url(r'^parties/$', views.list_parties, name='list_parties'),
                       url(r'^party/create/$', views.party_form, name='create_party'),
                       url(r'^party/(?P<id>[0-9]+)/delete/$', views.delete_party, name='delete_party'),
                       url(r'^party/(?P<id>[0-9]+)/$', views.party_form, name='update_party'),
                       url(r'^parties.json$', views.parties_as_json, name='parties_as_json'),

                       url(r'^employees/$', views.list_employees, name='list_employees'),
                       url(r'^employee/create/$', views.employee_form, name='create_party'),
                       url(r'^employee/(?P<id>[0-9]+)/delete/$', views.delete_employee, name='delete_employee'),
                       url(r'^employee/(?P<id>[0-9]+)/$', views.employee_form, name='update_employee'),
                       url(r'^employees.json$', views.employees_as_json, name='employees_as_json'),

)