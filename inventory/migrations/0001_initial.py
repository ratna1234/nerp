# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'inventory_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(blank=True, related_name='children', null=True, to=orm['inventory.Category'])),
            (u'lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal(u'inventory', ['Category'])

        # Adding model 'InventoryAccount'
        db.create_table(u'inventory_inventoryaccount', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('current_dr', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('current_cr', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('opening_balance', self.gf('django.db.models.fields.FloatField')(default=0)),
        ))
        db.send_create_signal(u'inventory', ['InventoryAccount'])

        # Adding model 'Item'
        db.create_table(u'inventory_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=254)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('purchase_price', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventory.Category'], null=True, blank=True)),
            ('account', self.gf('django.db.models.fields.related.OneToOneField')(related_name='item', unique=True, to=orm['inventory.InventoryAccount'])),
        ))
        db.send_create_signal(u'inventory', ['Item'])

        # Adding model 'JournalEntry'
        db.create_table(u'inventory_journalentry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='inventory_journal_entries', to=orm['contenttypes.ContentType'])),
            ('model_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'inventory', ['JournalEntry'])

        # Adding model 'Transaction'
        db.create_table(u'inventory_transaction', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('account', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventory.InventoryAccount'])),
            ('dr_amount', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('cr_amount', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('current_dr', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('current_cr', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('journal_entry', self.gf('django.db.models.fields.related.ForeignKey')(related_name='transactions', to=orm['inventory.JournalEntry'])),
        ))
        db.send_create_signal(u'inventory', ['Transaction'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'inventory_category')

        # Deleting model 'InventoryAccount'
        db.delete_table(u'inventory_inventoryaccount')

        # Deleting model 'Item'
        db.delete_table(u'inventory_item')

        # Deleting model 'JournalEntry'
        db.delete_table(u'inventory_journalentry')

        # Deleting model 'Transaction'
        db.delete_table(u'inventory_transaction')


    models = {
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
        u'inventory.inventoryaccount': {
            'Meta': {'object_name': 'InventoryAccount'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
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
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'purchase_price': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        u'inventory.journalentry': {
            'Meta': {'object_name': 'JournalEntry'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inventory_journal_entries'", 'to': u"orm['contenttypes.ContentType']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model_id': ('django.db.models.fields.IntegerField', [], {})
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
        }
    }

    complete_apps = ['inventory']