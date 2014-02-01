# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Account.name'
        db.delete_column(u'account_account', 'name')

        # Adding field 'Account.name_ne'
        db.add_column(u'account_account', 'name_ne',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=254),
                      keep_default=False)

        # Adding field 'Account.name_en'
        db.add_column(u'account_account', 'name_en',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=254),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Account.name'
        db.add_column(u'account_account', 'name',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=100),
                      keep_default=False)

        # Deleting field 'Account.name_ne'
        db.delete_column(u'account_account', 'name_ne')

        # Deleting field 'Account.name_en'
        db.delete_column(u'account_account', 'name_en')


    models = {
        u'account.account': {
            'Meta': {'object_name': 'Account'},
            'account_page_no': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'name_ne': ('django.db.models.fields.CharField', [], {'max_length': '254'})
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
        u'core.fiscalyear': {
            'Meta': {'object_name': 'FiscalYear'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['account']