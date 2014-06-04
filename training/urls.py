from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='training_index'),
                       url(r'^add/$', views.training_form, name='add_training'),
                       # url(r'^authors.json$', views.authors_as_json, name='authors_as_json'),
                       # url(r'^patron/(?P<pk>[0-9]+)/$', views.view_patron, name='view_patron'),
                       # url(r'^author/(?P<slug>[a-zA-Z0-9_.-]+)/$', views.view_author, name='view_author'),
                       # url(r'^search/(?P<keyword>.*)$', views.search, name='search'),
)
