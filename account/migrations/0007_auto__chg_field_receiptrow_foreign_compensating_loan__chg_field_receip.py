# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'ReceiptRow.foreign_compensating_loan'
        db.alter_column(u'account_receiptrow', 'foreign_compensating_loan', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'ReceiptRow.foreign_compensating_grant'
        db.alter_column(u'account_receiptrow', 'foreign_compensating_grant', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'ReceiptRow.foreign_cash_grant'
        db.alter_column(u'account_receiptrow', 'foreign_cash_grant', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'ReceiptRow.nepal_government'
        db.alter_column(u'account_receiptrow', 'nepal_government', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'ReceiptRow.foreign_substantial_aid'
        db.alter_column(u'account_receiptrow', 'foreign_substantial_aid', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'ReceiptRow.foreign_cash_loan'
        db.alter_column(u'account_receiptrow', 'foreign_cash_loan', self.gf('django.db.models.fields.FloatField')(null=True))

    def backwards(self, orm):

        # Changing field 'ReceiptRow.foreign_compensating_loan'
        db.alter_column(u'account_receiptrow', 'foreign_compensating_loan', self.gf('django.db.models.fields.FloatField')())

        # Changing field 'ReceiptRow.foreign_compensating_grant'
        db.alter_column(u'account_receiptrow', 'foreign_compensating_grant', self.gf('django.db.models.fields.FloatField')())

        # Changing field 'ReceiptRow.foreign_cash_grant'
        db.alter_column(u'account_receiptrow', 'foreign_cash_grant', self.gf('django.db.models.fields.FloatField')())

        # Changing field 'ReceiptRow.nepal_government'
        db.alter_column(u'account_receiptrow', 'nepal_government', self.gf('django.db.models.fields.FloatField')())

        # Changing field 'ReceiptRow.foreign_substantial_aid'
        db.alter_column(u'account_receiptrow', 'foreign_substantial_aid', self.gf('django.db.models.fields.FloatField')())

        # Changing field 'ReceiptRow.foreign_cash_loan'
        db.alter_column(u'account_receiptrow', 'foreign_cash_loan', self.gf('django.db.models.fields.FloatField')())

    models = {
        u'account.journalvoucher': {
            'Meta': {'object_name': 'JournalVoucher'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'fiscal_year': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.FiscalYear']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'voucher_no': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        u'account.journalvoucherrow': {
            'Meta': {'object_name': 'JournalVoucherRow'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Account']"}),
            'cr_amount': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dr_amount': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'account.receipt': {
            'Meta': {'object_name': 'Receipt'},
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'no': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        u'account.receiptrow': {
            'Meta': {'object_name': 'ReceiptRow'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Account']"}),
            'activity': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Activity']", 'null': 'True', 'blank': 'True'}),
            'advanced': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'advanced_settlement': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'budget': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Budget']"}),
            'cash_returned': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'donor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Donor']", 'null': 'True', 'blank': 'True'}),
            'foreign_cash_grant': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'foreign_cash_loan': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'foreign_compensating_grant': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'foreign_compensating_loan': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'foreign_substantial_aid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice_no': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nepal_government': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'receipt': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rows'", 'to': u"orm['account.Receipt']"}),
            'remarks': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'sn': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'vattable': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'core.account': {
            'Meta': {'object_name': 'Account'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'name_ne': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'})
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