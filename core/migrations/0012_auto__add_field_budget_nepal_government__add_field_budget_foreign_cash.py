# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Budget.nepal_government'
        db.add_column(u'core_budget', 'nepal_government',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Budget.foreign_cash_grant'
        db.add_column(u'core_budget', 'foreign_cash_grant',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Budget.foreign_compensating_grant'
        db.add_column(u'core_budget', 'foreign_compensating_grant',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Budget.foreign_cash_loan'
        db.add_column(u'core_budget', 'foreign_cash_loan',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Budget.foreign_compensating_loan'
        db.add_column(u'core_budget', 'foreign_compensating_loan',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Budget.foreign_substantial_aid'
        db.add_column(u'core_budget', 'foreign_substantial_aid',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Budget.nepal_government'
        db.delete_column(u'core_budget', 'nepal_government')

        # Deleting field 'Budget.foreign_cash_grant'
        db.delete_column(u'core_budget', 'foreign_cash_grant')

        # Deleting field 'Budget.foreign_compensating_grant'
        db.delete_column(u'core_budget', 'foreign_compensating_grant')

        # Deleting field 'Budget.foreign_cash_loan'
        db.delete_column(u'core_budget', 'foreign_cash_loan')

        # Deleting field 'Budget.foreign_compensating_loan'
        db.delete_column(u'core_budget', 'foreign_compensating_loan')

        # Deleting field 'Budget.foreign_substantial_aid'
        db.delete_column(u'core_budget', 'foreign_substantial_aid')


    models = {
        u'core.activity': {
            'Meta': {'object_name': 'Activity'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'name_ne': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'no': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        u'core.appsetting': {
            'Meta': {'object_name': 'AppSetting'},
            'app_name': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'fiscal_year': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.FiscalYear']"}),
            'header_for_forms': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'core.budget': {
            'Meta': {'object_name': 'Budget'},
            'foreign_cash_grant': ('django.db.models.fields.FloatField', [], {}),
            'foreign_cash_loan': ('django.db.models.fields.FloatField', [], {}),
            'foreign_compensating_grant': ('django.db.models.fields.FloatField', [], {}),
            'foreign_compensating_loan': ('django.db.models.fields.FloatField', [], {}),
            'foreign_substantial_aid': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'name_ne': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'nepal_government': ('django.db.models.fields.FloatField', [], {}),
            'no': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        u'core.donor': {
            'Meta': {'object_name': 'Donor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'core.employee': {
            'Meta': {'object_name': 'Employee'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'name_ne': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'})
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
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'name_ne': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'pan_no': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'phone_no': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['core']