from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='training_index'),
                       url(r'^add/$', views.training_form, name='add_training'),
                       url(r'^(?P<pk>[0-9]+)/$', views.training_form, name='update_training'),
                       url(r'^category/add/$', views.category_form, name='add_category'),
                       url(r'^category/(?P<pk>[0-9]+)/$', views.category_form, name='update_category'),
                       url(r'^resource_person/add/$', views.resource_person_form, name='add_resource_person'),
                       url(r'^resource_person/(?P<pk>[0-9]+)/$', views.resource_person_form,
                           name='update_resource_person'),
                       url(r'^target_group/add/$', views.target_group_form, name='add_target_group'),
                       url(r'^target_group/(?P<pk>[0-9]+)/$', views.target_group_form, name='update_target_group'),
                       url(r'^participants.json$', views.participants_as_json, name='participants_as_json'),
                       # url(r'^authors.json$', views.authors_as_json, name='authors_as_json'),
                       # url(r'^patron/(?P<pk>[0-9]+)/$', views.view_patron, name='view_patron'),
                       # url(r'^author/(?P<slug>[a-zA-Z0-9_.-]+)/$', views.view_author, name='view_author'),
                       # url(r'^search/(?P<keyword>.*)$', views.search, name='search'),
)
