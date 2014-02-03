from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',

                       # url(r'^receipts/$', views.list_receipts, name='list_receipts'),
                       url(r'^receipt/create/$', views.receipt, name='create_receipt'),
                       url(r'^receipt/(?P<id>[0-9]+)/$', views.receipt, name='update_receipt'),
                       # url(r'^receipt/(?P<id>[0-9]+)/delete/$', views.delete_receipt, name='delete_receipt'),




)
