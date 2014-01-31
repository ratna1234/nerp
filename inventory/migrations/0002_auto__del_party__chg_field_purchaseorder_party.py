# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Party'
        db.delete_table(u'inventory_party')


        # Changing field 'PurchaseOrder.party'
        db.alter_column(u'inventory_purchaseorder', 'party_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Party']))

    def backwards(self, orm):
        # Adding model 'Party'
        db.create_table(u'inventory_party', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=254)),
            ('pan_no', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('phone_no', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'inventory', ['Party'])


        # Changing field 'PurchaseOrder.party'
        db.alter_column(u'inventory_purchaseorder', 'party_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventory.Party']))

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'core.fiscalyear': {
            'Meta': {'object_name': 'FiscalYear'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        u'core.party': {
            'Meta': {'object_name': 'Party'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'pan_no': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'phone_no': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'inventory.category': {
            'Meta': {'object_name': 'Category'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['inventory.Category']"}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        u'inventory.demand': {
            'Meta': {'object_name': 'Demand'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'demandee': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.User']"}),
            'fiscal_year': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.FiscalYear']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'purpose': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'release_no': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'inventory.demandrow': {
            'Meta': {'object_name': 'DemandRow'},
            'demand': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rows'", 'to': u"orm['inventory.Demand']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.Item']"}),
            'quantity': ('django.db.models.fields.FloatField', [], {}),
            'release_quantity': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'remarks': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'sn': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'specification': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'Requested'", 'max_length': '9'}),
            'unit': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'inventory.entryreport': {
            'Meta': {'object_name': 'EntryReport'},
            'entry_report_no': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'fiscal_year': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.FiscalYear']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'source_content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            'source_object_id': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        u'inventory.entryreportrow': {
            'Meta': {'object_name': 'EntryReportRow'},
            'entry_report': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rows'", 'to': u"orm['inventory.EntryReport']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.Item']"}),
            'other_expenses': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'quantity': ('django.db.models.fields.FloatField', [], {}),
            'rate': ('django.db.models.fields.FloatField', [], {}),
            'remarks': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'sn': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'specification': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'unit': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'inventory.handover': {
            'Meta': {'object_name': 'Handover'},
            'addressee': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'designation': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'due_days': ('django.db.models.fields.PositiveIntegerField', [], {'default': '7'}),
            'fiscal_year': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.FiscalYear']"}),
            'handed_to': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'office': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'Incoming'", 'max_length': '9'}),
            'voucher_no': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        u'inventory.handoverrow': {
            'Meta': {'object_name': 'HandoverRow'},
            'condition': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'handover': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rows'", 'to': u"orm['inventory.Handover']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.Item']"}),
            'quantity': ('django.db.models.fields.FloatField', [], {}),
            'received_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'sn': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'specification': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'total_amount': ('django.db.models.fields.FloatField', [], {}),
            'unit': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'inventory.inventoryaccount': {
            'Meta': {'object_name': 'InventoryAccount'},
            'account_no': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'current_balance': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'opening_balance': ('django.db.models.fields.FloatField', [], {'default': '0'})
        },
        u'inventory.inventoryaccountrow': {
            'Meta': {'object_name': 'InventoryAccountRow'},
            'country_of_production_or_company_name': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'expected_life': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'expense_total_cost_price': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'journal_entry': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'account_row'", 'unique': 'True', 'to': u"orm['inventory.JournalEntry']"}),
            'remaining_total_cost_price': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'remarks': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'})
        },
        u'inventory.item': {
            'Meta': {'object_name': 'Item'},
            'account': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'item'", 'unique': 'True', 'to': u"orm['inventory.InventoryAccount']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.Category']", 'null': 'True', 'blank': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'property_classification_reference_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'consumable'", 'max_length': '15'}),
            'unit': ('django.db.models.fields.CharField', [], {'default': "u'pieces'", 'max_length': '50'}),
            'vattable': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'inventory.journalentry': {
            'Meta': {'object_name': 'JournalEntry'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inventory_journal_entries'", 'to': u"orm['contenttypes.ContentType']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model_id': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        u'inventory.purchaseorder': {
            'Meta': {'object_name': 'PurchaseOrder'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'due_days': ('django.db.models.fields.IntegerField', [], {'default': '3'}),
            'fiscal_year': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.FiscalYear']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order_no': ('django.db.models.fields.IntegerField', [], {}),
            'party': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Party']"})
        },
        u'inventory.purchaseorderrow': {
            'Meta': {'object_name': 'PurchaseOrderRow'},
            'budget_title_no': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.Item']"}),
            'purchase_order': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rows'", 'to': u"orm['inventory.PurchaseOrder']"}),
            'quantity': ('django.db.models.fields.FloatField', [], {}),
            'rate': ('django.db.models.fields.FloatField', [], {}),
            'remarks': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'sn': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'specification': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'unit': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'inventory.transaction': {
            'Meta': {'object_name': 'Transaction'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.InventoryAccount']"}),
            'cr_amount': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'current_balance': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dr_amount': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'journal_entry': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'transactions'", 'to': u"orm['inventory.JournalEntry']"})
        },
        u'users.user': {
            'Meta': {'object_name': 'User'},
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '254', 'db_index': 'True'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '245'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'users'", 'symmetrical': 'False', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['inventory']