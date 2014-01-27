# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
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
            ('code', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('account_no', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('current_balance', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('opening_balance', self.gf('django.db.models.fields.FloatField')(default=0)),
        ))
        db.send_create_signal(u'inventory', ['InventoryAccount'])

        # Adding model 'Item'
        db.create_table(u'inventory_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=254)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventory.Category'], null=True, blank=True)),
            ('account', self.gf('django.db.models.fields.related.OneToOneField')(related_name='item', unique=True, to=orm['inventory.InventoryAccount'])),
            ('type', self.gf('django.db.models.fields.CharField')(default='consumable', max_length=15)),
            ('unit', self.gf('django.db.models.fields.CharField')(default=u'pieces', max_length=50)),
            ('vattable', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('property_classification_reference_number', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
        ))
        db.send_create_signal(u'inventory', ['Item'])

        # Adding model 'JournalEntry'
        db.create_table(u'inventory_journalentry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='inventory_journal_entries', to=orm['contenttypes.ContentType'])),
            ('model_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'inventory', ['JournalEntry'])

        # Adding model 'Transaction'
        db.create_table(u'inventory_transaction', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('account', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventory.InventoryAccount'])),
            ('dr_amount', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('cr_amount', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('current_balance', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('journal_entry', self.gf('django.db.models.fields.related.ForeignKey')(related_name='transactions', to=orm['inventory.JournalEntry'])),
        ))
        db.send_create_signal(u'inventory', ['Transaction'])

        # Adding model 'Demand'
        db.create_table(u'inventory_demand', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('release_no', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('fiscal_year', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.FiscalYear'])),
            ('demandee', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.User'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('purpose', self.gf('django.db.models.fields.CharField')(max_length=254)),
        ))
        db.send_create_signal(u'inventory', ['Demand'])

        # Adding model 'DemandRow'
        db.create_table(u'inventory_demandrow', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sn', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventory.Item'])),
            ('specification', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('quantity', self.gf('django.db.models.fields.FloatField')()),
            ('unit', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('release_quantity', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('remarks', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('demand', self.gf('django.db.models.fields.related.ForeignKey')(related_name='rows', to=orm['inventory.Demand'])),
            ('status', self.gf('django.db.models.fields.CharField')(default='Requested', max_length=9)),
        ))
        db.send_create_signal(u'inventory', ['DemandRow'])

        # Adding model 'Party'
        db.create_table(u'inventory_party', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=254)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('phone_no', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('pan_no', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal(u'inventory', ['Party'])

        # Adding model 'EntryReport'
        db.create_table(u'inventory_entryreport', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('entry_report_no', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('fiscal_year', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.FiscalYear'])),
            ('source_content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('source_object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'inventory', ['EntryReport'])

        # Adding model 'EntryReportRow'
        db.create_table(u'inventory_entryreportrow', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sn', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventory.Item'])),
            ('specification', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('quantity', self.gf('django.db.models.fields.FloatField')()),
            ('unit', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('rate', self.gf('django.db.models.fields.FloatField')()),
            ('other_expenses', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('remarks', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('entry_report', self.gf('django.db.models.fields.related.ForeignKey')(related_name='rows', to=orm['inventory.EntryReport'])),
        ))
        db.send_create_signal(u'inventory', ['EntryReportRow'])

        # Adding model 'Handover'
        db.create_table(u'inventory_handover', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('voucher_no', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('addressee', self.gf('django.db.models.fields.CharField')(max_length=254)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('office', self.gf('django.db.models.fields.CharField')(max_length=254)),
            ('designation', self.gf('django.db.models.fields.CharField')(max_length=254)),
            ('handed_to', self.gf('django.db.models.fields.CharField')(max_length=254)),
            ('due_days', self.gf('django.db.models.fields.PositiveIntegerField')(default=7)),
            ('fiscal_year', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.FiscalYear'])),
            ('type', self.gf('django.db.models.fields.CharField')(default='Incoming', max_length=9)),
        ))
        db.send_create_signal(u'inventory', ['Handover'])

        # Adding model 'HandoverRow'
        db.create_table(u'inventory_handoverrow', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sn', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventory.Item'])),
            ('specification', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('quantity', self.gf('django.db.models.fields.FloatField')()),
            ('unit', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('total_amount', self.gf('django.db.models.fields.FloatField')()),
            ('received_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('condition', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('handover', self.gf('django.db.models.fields.related.ForeignKey')(related_name='rows', to=orm['inventory.Handover'])),
        ))
        db.send_create_signal(u'inventory', ['HandoverRow'])

        # Adding model 'PurchaseOrder'
        db.create_table(u'inventory_purchaseorder', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('party', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventory.Party'])),
            ('order_no', self.gf('django.db.models.fields.IntegerField')()),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('due_days', self.gf('django.db.models.fields.IntegerField')(default=3)),
            ('fiscal_year', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.FiscalYear'])),
        ))
        db.send_create_signal(u'inventory', ['PurchaseOrder'])

        # Adding model 'PurchaseOrderRow'
        db.create_table(u'inventory_purchaseorderrow', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sn', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('budget_title_no', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventory.Item'])),
            ('specification', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('quantity', self.gf('django.db.models.fields.FloatField')()),
            ('unit', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('rate', self.gf('django.db.models.fields.FloatField')()),
            ('remarks', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('purchase_order', self.gf('django.db.models.fields.related.ForeignKey')(related_name='rows', to=orm['inventory.PurchaseOrder'])),
        ))
        db.send_create_signal(u'inventory', ['PurchaseOrderRow'])

        # Adding model 'InventoryAccountRow'
        db.create_table(u'inventory_inventoryaccountrow', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('country_of_production_or_company_name', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('size', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('expected_life', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('expense_total_cost_price', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('remaining_total_cost_price', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('remarks', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('journal_entry', self.gf('django.db.models.fields.related.OneToOneField')(related_name='account_row', unique=True, to=orm['inventory.JournalEntry'])),
        ))
        db.send_create_signal(u'inventory', ['InventoryAccountRow'])


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

        # Deleting model 'Demand'
        db.delete_table(u'inventory_demand')

        # Deleting model 'DemandRow'
        db.delete_table(u'inventory_demandrow')

        # Deleting model 'Party'
        db.delete_table(u'inventory_party')

        # Deleting model 'EntryReport'
        db.delete_table(u'inventory_entryreport')

        # Deleting model 'EntryReportRow'
        db.delete_table(u'inventory_entryreportrow')

        # Deleting model 'Handover'
        db.delete_table(u'inventory_handover')

        # Deleting model 'HandoverRow'
        db.delete_table(u'inventory_handoverrow')

        # Deleting model 'PurchaseOrder'
        db.delete_table(u'inventory_purchaseorder')

        # Deleting model 'PurchaseOrderRow'
        db.delete_table(u'inventory_purchaseorderrow')

        # Deleting model 'InventoryAccountRow'
        db.delete_table(u'inventory_inventoryaccountrow')


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
            'fiscal_year': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.FiscalYear']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order_no': ('django.db.models.fields.IntegerField', [], {}),
            'party': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.Party']"})
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