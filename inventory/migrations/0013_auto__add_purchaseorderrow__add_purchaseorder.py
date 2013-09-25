# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PurchaseOrderRow'
        db.create_table(u'inventory_purchaseorderrow', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sn', self.gf('django.db.models.fields.IntegerField')()),
            ('budget_title_no', self.gf('django.db.models.fields.IntegerField')()),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventory.Item'])),
            ('specification', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('quantity', self.gf('django.db.models.fields.FloatField')()),
            ('unit', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('rate', self.gf('django.db.models.fields.FloatField')()),
            ('remarks', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('purchase_order', self.gf('django.db.models.fields.related.ForeignKey')(related_name='rows', to=orm['inventory.PurchaseOrder'])),
        ))
        db.send_create_signal(u'inventory', ['PurchaseOrderRow'])

        # Adding model 'PurchaseOrder'
        db.create_table(u'inventory_purchaseorder', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('party', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventory.Party'])),
            ('order_no', self.gf('django.db.models.fields.IntegerField')()),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('due_days', self.gf('django.db.models.fields.IntegerField')(default=3)),
        ))
        db.send_create_signal(u'inventory', ['PurchaseOrder'])


    def backwards(self, orm):
        # Deleting model 'PurchaseOrderRow'
        db.delete_table(u'inventory_purchaseorderrow')

        # Deleting model 'PurchaseOrder'
        db.delete_table(u'inventory_purchaseorder')


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
            'fiscal_year': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'purpose': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'release_no': ('django.db.models.fields.IntegerField', [], {})
        },
        u'inventory.demandrow': {
            'Meta': {'object_name': 'DemandRow'},
            'demand': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rows'", 'to': u"orm['inventory.Demand']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.Item']"}),
            'quantity': ('django.db.models.fields.FloatField', [], {}),
            'release_quantity': ('django.db.models.fields.FloatField', [], {}),
            'remarks': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'sn': ('django.db.models.fields.IntegerField', [], {}),
            'specification': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'unit': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'inventory.inventoryaccount': {
            'Meta': {'object_name': 'InventoryAccount'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'current_cr': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'current_dr': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'opening_balance': ('django.db.models.fields.FloatField', [], {'default': '0'})
        },
        u'inventory.item': {
            'Meta': {'object_name': 'Item'},
            'account': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'item'", 'unique': 'True', 'to': u"orm['inventory.InventoryAccount']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.Category']", 'null': 'True', 'blank': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'purchase_price': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'consumable'", 'max_length': '15'}),
            'unit': ('django.db.models.fields.CharField', [], {'default': "u'pieces'", 'max_length': '50'}),
            'vattable': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'inventory.journalentry': {
            'Meta': {'object_name': 'JournalEntry'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inventory_journal_entries'", 'to': u"orm['contenttypes.ContentType']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model_id': ('django.db.models.fields.IntegerField', [], {})
        },
        u'inventory.party': {
            'Meta': {'object_name': 'Party'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'pan_no': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'phone_no': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'inventory.purchaseorder': {
            'Meta': {'object_name': 'PurchaseOrder'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'due_days': ('django.db.models.fields.IntegerField', [], {'default': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order_no': ('django.db.models.fields.IntegerField', [], {}),
            'party': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.Party']"})
        },
        u'inventory.purchaseorderrow': {
            'Meta': {'object_name': 'PurchaseOrderRow'},
            'budget_title_no': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.Item']"}),
            'purchase_order': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rows'", 'to': u"orm['inventory.PurchaseOrder']"}),
            'quantity': ('django.db.models.fields.FloatField', [], {}),
            'rate': ('django.db.models.fields.FloatField', [], {}),
            'remarks': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'sn': ('django.db.models.fields.IntegerField', [], {}),
            'specification': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'unit': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'inventory.transaction': {
            'Meta': {'object_name': 'Transaction'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.InventoryAccount']"}),
            'cr_amount': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'current_cr': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'current_dr': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dr_amount': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'journal_entry': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'transactions'", 'to': u"orm['inventory.JournalEntry']"})
        },
        u'users.user': {
            'Meta': {'object_name': 'User', 'db_table': "u'user'"},
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '254', 'db_index': 'True'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '245'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'users'", 'symmetrical': 'False', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['inventory']