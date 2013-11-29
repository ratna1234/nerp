from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
                       url(r'^items/$', views.list_inventory_items, name='list_inventory_items'),
                       url(r'^create/$', views.item_form, name='create_inventory_item'),
                       url(r'^item/delete/(?P<id>[0-9]+)/$', views.delete_inventory_item, name='delete_inventory_item'),
                       url(r'^(?P<id>[0-9]+)/$', views.item_form, name='update_inventory_item'),
                       url(r'^items.json$', views.items_as_json, name='items_as_json'),

                       url(r'^accounts/$', views.list_inventory_accounts, name='list_inventory_accounts'),
                       url(r'^account/(?P<id>[0-9]+)/$', views.view_inventory_account, name='view_inventory_account'),

                       url(r'^categories/$', views.list_categories, name='list_inventory_categories'),
                       url(r'^category/create/$', views.create_category, name='create_inventory_category'),
                       url(r'^category/(?P<id>[0-9]+)/$', views.update_category, name='update_inventory_category'),
                       url(r'^category/(?P<id>[0-9]+)/delete$', views.delete_category,
                           name='delete_inventory_category'),

                       url(r'^demand/$', views.demand_form, name='create_demand_form'),
                       url(r'^demand/(?P<id>[0-9]+)/$', views.demand_form, name='update_demand_form'),
                       url(r'^save/demand_form/$', views.save_demand, name='save_demand_form'),
                       url(r'^demand/(?P<id>[0-9]+)/delete$', views.delete_demand,
                           name='delete_demand_form'),
                       url(r'^demand-forms/$', views.list_demand_forms, name='list_demand_forms'),

                       url(r'^parties/$', views.list_parties, name='list_parties'),
                       url(r'^party/create/$', views.party_form, name='create_party'),
                       url(r'^party/(?P<id>[0-9]+)/delete/$', views.delete_party, name='delete_party'),
                       url(r'^party/(?P<id>[0-9]+)/$', views.party_form, name='update_party'),
                       url(r'^parties.json$', views.parties_as_json, name='parties_as_json'),

                       url(r'^purchase-order/$', views.purchase_order, name='create_purchase_order'),
                       url(r'^purchase-order/(?P<id>[0-9]+)/$', views.purchase_order, name='update_purchase_order'),
                       url(r'^save/purchase_order/$', views.save_purchase_order, name='save_purchase_order'),
                       url(r'^purchase-order/(?P<id>[0-9]+)/delete$', views.delete_purchase_order,
                           name='delete_purchase_order'),
                       url(r'^purchase-orders/$', views.list_purchase_orders, name='list_purchase_orders'),

                       #url(r'^entry-report/$', views.entry_report, name='create_entry_report'),
                       #url(r'^purchase-order/(?P<id>[0-9]+)/$', views.purchase_order, name='update_purchase_order'),
                       #url(r'^save/purchase_order/$', views.save_purchase_order, name='save_purchase_order'),
                       #url(r'^purchase-order/(?P<id>[0-9]+)/delete$', views.delete_purchase_order,
                       #    name='delete_purchase_order'),
                       #url(r'^purchase-orders/$', views.list_purchase_orders, name='list_purchase_orders'),

)

