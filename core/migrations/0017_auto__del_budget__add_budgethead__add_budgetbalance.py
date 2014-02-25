# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Budget'
        db.delete_table(u'core_budget')

        # Adding model 'BudgetHead'
        db.create_table(u'core_budgethead', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name_ne', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('name_en', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('no', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'core', ['BudgetHead'])

        # Adding model 'BudgetBalance'
        db.create_table(u'core_budgetbalance', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('budget_head', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.BudgetHead'])),
            ('fiscal_year', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.FiscalYear'])),
            ('nepal_government', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('foreign_cash_grant', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('foreign_compensating_grant', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('foreign_cash_loan', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('foreign_compensating_loan', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('foreign_substantial_aid', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('nepal_government_due', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('foreign_cash_grant_due', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('foreign_compensating_grant_due', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('foreign_cash_loan_due', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('foreign_compensating_loan_due', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('foreign_substantial_aid_due', self.gf('django.db.models.fields.FloatField')(default=0)),
        ))
        db.send_create_signal(u'core', ['BudgetBalance'])


    def backwards(self, orm):
        # Adding model 'Budget'
        db.create_table(u'core_budget', (
            ('foreign_compensating_grant', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('foreign_substantial_aid', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('nepal_government', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('name_en', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('foreign_compensating_loan', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('foreign_cash_grant', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('no', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('name_ne', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('foreign_cash_loan', self.gf('django.db.models.fields.FloatField')(default=0)),
        ))
        db.send_create_signal(u'core', ['Budget'])

        # Deleting model 'BudgetHead'
        db.delete_table(u'core_budgethead')

        # Deleting model 'BudgetBalance'
        db.delete_table(u'core_budgetbalance')


    models = {
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
        u'core.appsetting': {
            'Meta': {'object_name': 'AppSetting'},
            'app_name': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'fiscal_year': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.FiscalYear']"}),
            'header_for_forms': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'core.budgetbalance': {
            'Meta': {'object_name': 'BudgetBalance'},
            'budget_head': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.BudgetHead']"}),
            'fiscal_year': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.FiscalYear']"}),
            'foreign_cash_grant': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'foreign_cash_grant_due': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'foreign_cash_loan': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'foreign_cash_loan_due': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'foreign_compensating_grant': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'foreign_compensating_grant_due': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'foreign_compensating_loan': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'foreign_compensating_loan_due': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'foreign_substantial_aid': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'foreign_substantial_aid_due': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nepal_government': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'nepal_government_due': ('django.db.models.fields.FloatField', [], {'default': '0'})
        },
        u'core.budgethead': {
            'Meta': {'object_name': 'BudgetHead'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'name_ne': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'no': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        u'core.donor': {
            'Meta': {'object_name': 'Donor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'name_ne': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'})
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
            'account': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'party'", 'unique': 'True', 'to': u"orm['core.Account']"}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'name_ne': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'pan_no': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'phone_no': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'core.taxscheme': {
            'Meta': {'object_name': 'TaxScheme'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'name_ne': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'percent': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['core']