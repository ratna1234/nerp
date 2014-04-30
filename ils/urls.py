from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',

                       url(r'^acquisition/$', views.acquisition, name='acquisition'),
                       url(r'^authors.json$', views.authors_as_json, name='authors_as_json'),
                       url(r'^publishers.json$', views.publishers_as_json, name='publishers_as_json'),
                       url(r'^subjects.json$', views.subjects_as_json, name='subjects_as_json'),
                       url(r'^books.json$', views.books_as_json, name='books_as_json'),
                       # url(r'^receipt/(?P<pk>[0-9]+)/$', views.receipt, name='update_receipt'),
                       # # url(r'^receipt/(?P<id>[0-9]+)/delete/$', views.delete_receipt, name='delete_receipt'),
                       url(r'^acquisition/save/$', views.save_acquisition, name='save_acquisition'),
                       url(r'^outgoing/$', views.outgoing, name='outgoing'),
                       url(r'^incoming/(?P<transaction_pk>[0-9]+)$', views.incoming, name='incoming'),
                       url(r'^outgoing/save$', views.save_outgoing, name='save_outgoing'),
                       url(r'^record/(?P<pk>[0-9]+)/$', views.view_record, name='view_record'),
                       url(r'^patrons/$', views.list_patrons, name='list_patrons'),
                       url(r'^patron/(?P<pk>[0-9]+)/$', views.view_patron, name='view_patron'),
                       url(r'^transactions/$', views.list_transactions, name='list_transactions'),
                       url(r'^records/$', views.list_records, name='list_records'),
                       url(r'^author/(?P<slug>[a-zA-Z0-9_.-]+)/$', views.view_author, name='view_author'),
                       url(r'^authors/$', views.list_authors, name='list_authors'),
                       url(r'^publisher/(?P<slug>[a-zA-Z0-9_.-]+)/$', views.view_publisher, name='view_publisher'),
                       url(r'^publishers/$', views.list_publishers, name='list_publishers'),

)
