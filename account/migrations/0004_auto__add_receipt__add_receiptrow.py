# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Receipt'
        db.create_table(u'account_receipt', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'account', ['Receipt'])

        # Adding model 'ReceiptRow'
        db.create_table(u'account_receiptrow', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sn', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('budget', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Budget'])),
            ('account', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['account.Account'])),
            ('invoice_no', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('vattable', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('nepal_government', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('foreign_cash_grant', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('foreign_compensating_grant', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('foreign_cash_loan', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('foreign_compensating_loan', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('foreign_substantial_aid', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('donor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Donor'], null=True, blank=True)),
            ('advanced', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('advanced_settlement', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('cash_returned', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('activity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Activity'], null=True, blank=True)),
            ('remarks', self.gf('django.db.models.fields.CharField')(max_length=254)),
            ('receipt', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['account.Receipt'])),
        ))
        db.send_create_signal(u'account', ['ReceiptRow'])


    def backwards(self, orm):
        # Deleting model 'Receipt'
        db.delete_table(u'account_receipt')

        # Deleting model 'ReceiptRow'
        db.delete_table(u'account_receiptrow')


    models = {
        u'account.account': {
            'Meta': {'object_name': 'Account'},
            'account_page_no': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'name_ne': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'})
        },
        u'account.journalvoucher': {
            'Meta': {'object_name': 'JournalVoucher'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'fiscal_year': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.FiscalYear']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'voucher_no': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        u'account.journalvoucherrow': {
            'Meta': {'object_name': 'JournalVoucherRow'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['account.Account']"}),
            'cr_amount': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dr_amount': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'account.receipt': {
            'Meta': {'object_name': 'Receipt'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'account.receiptrow': {
            'Meta': {'object_name': 'ReceiptRow'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['account.Account']"}),
            'activity': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Activity']", 'null': 'True', 'blank': 'True'}),
            'advanced': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'advanced_settlement': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'budget': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Budget']"}),
            'cash_returned': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'donor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Donor']", 'null': 'True', 'blank': 'True'}),
            'foreign_cash_grant': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'foreign_cash_loan': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'foreign_compensating_grant': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'foreign_compensating_loan': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'foreign_substantial_aid': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice_no': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nepal_government': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'receipt': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['account.Receipt']"}),
            'remarks': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'sn': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'vattable': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'core.activity': {
            'Meta': {'object_name': 'Activity'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'name_ne': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'no': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        u'core.budget': {
            'Meta': {'object_name': 'Budget'},
            'foreign_cash_grant': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'foreign_cash_loan': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'foreign_compensating_grant': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'foreign_compensating_loan': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'foreign_substantial_aid': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'name_ne': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'nepal_government': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'no': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        u'core.donor': {
            'Meta': {'object_name': 'Donor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'name_ne': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'})
        },
        u'core.fiscalyear': {
            'Meta': {'object_name': 'FiscalYear'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['account']