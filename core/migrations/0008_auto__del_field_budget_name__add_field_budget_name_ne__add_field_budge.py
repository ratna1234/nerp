# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Budget.name'
        db.delete_column(u'core_budget', 'name')

        # Adding field 'Budget.name_ne'
        db.add_column(u'core_budget', 'name_ne',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=254),
                      keep_default=False)

        # Adding field 'Budget.name_en'
        db.add_column(u'core_budget', 'name_en',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=254),
                      keep_default=False)

        # Deleting field 'Activity.name'
        db.delete_column(u'core_activity', 'name')

        # Adding field 'Activity.name_ne'
        db.add_column(u'core_activity', 'name_ne',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=254),
                      keep_default=False)

        # Adding field 'Activity.name_en'
        db.add_column(u'core_activity', 'name_en',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=254),
                      keep_default=False)

        # Deleting field 'Donor.name'
        db.delete_column(u'core_donor', 'name')

        # Deleting field 'Employee.name'
        db.delete_column(u'core_employee', 'name')

        # Adding field 'Employee.name_ne'
        db.add_column(u'core_employee', 'name_ne',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=254),
                      keep_default=False)

        # Adding field 'Employee.name_en'
        db.add_column(u'core_employee', 'name_en',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=254),
                      keep_default=False)

        # Deleting field 'Party.name'
        db.delete_column(u'core_party', 'name')

        # Adding field 'Party.name_ne'
        db.add_column(u'core_party', 'name_ne',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=254),
                      keep_default=False)

        # Adding field 'Party.name_en'
        db.add_column(u'core_party', 'name_en',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=254),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Budget.name'
        db.add_column(u'core_budget', 'name',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=254),
                      keep_default=False)

        # Deleting field 'Budget.name_ne'
        db.delete_column(u'core_budget', 'name_ne')

        # Deleting field 'Budget.name_en'
        db.delete_column(u'core_budget', 'name_en')

        # Adding field 'Activity.name'
        db.add_column(u'core_activity', 'name',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=254),
                      keep_default=False)

        # Deleting field 'Activity.name_ne'
        db.delete_column(u'core_activity', 'name_ne')

        # Deleting field 'Activity.name_en'
        db.delete_column(u'core_activity', 'name_en')

        # Adding field 'Donor.name'
        db.add_column(u'core_donor', 'name',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=254),
                      keep_default=False)

        # Adding field 'Employee.name'
        db.add_column(u'core_employee', 'name',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=254),
                      keep_default=False)

        # Deleting field 'Employee.name_ne'
        db.delete_column(u'core_employee', 'name_ne')

        # Deleting field 'Employee.name_en'
        db.delete_column(u'core_employee', 'name_en')

        # Adding field 'Party.name'
        db.add_column(u'core_party', 'name',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=254),
                      keep_default=False)

        # Deleting field 'Party.name_ne'
        db.delete_column(u'core_party', 'name_ne')

        # Deleting field 'Party.name_en'
        db.delete_column(u'core_party', 'name_en')


    models = {
        u'core.activity': {
            'Meta': {'object_name': 'Activity'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'name_ne': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'name_ne': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'no': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        u'core.donor': {
            'Meta': {'object_name': 'Donor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'core.employee': {
            'Meta': {'object_name': 'Employee'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'name_ne': ('django.db.models.fields.CharField', [], {'max_length': '254'})
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
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'name_ne': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'pan_no': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'phone_no': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['core']