# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Budget.name_en'
        db.alter_column(u'core_budget', 'name_en', self.gf('django.db.models.fields.CharField')(max_length=254, null=True))

        # Changing field 'Budget.name_ne'
        db.alter_column(u'core_budget', 'name_ne', self.gf('django.db.models.fields.CharField')(max_length=254, null=True))

        # Changing field 'Activity.name_en'
        db.alter_column(u'core_activity', 'name_en', self.gf('django.db.models.fields.CharField')(max_length=254, null=True))

        # Changing field 'Activity.name_ne'
        db.alter_column(u'core_activity', 'name_ne', self.gf('django.db.models.fields.CharField')(max_length=254, null=True))

        # Changing field 'Employee.name_en'
        db.alter_column(u'core_employee', 'name_en', self.gf('django.db.models.fields.CharField')(max_length=254, null=True))

        # Changing field 'Employee.name_ne'
        db.alter_column(u'core_employee', 'name_ne', self.gf('django.db.models.fields.CharField')(max_length=254, null=True))

        # Changing field 'Party.name_ne'
        db.alter_column(u'core_party', 'name_ne', self.gf('django.db.models.fields.CharField')(max_length=254, null=True))

        # Changing field 'Party.name_en'
        db.alter_column(u'core_party', 'name_en', self.gf('django.db.models.fields.CharField')(max_length=254, null=True))

    def backwards(self, orm):

        # Changing field 'Budget.name_en'
        db.alter_column(u'core_budget', 'name_en', self.gf('django.db.models.fields.CharField')(default=None, max_length=254))

        # Changing field 'Budget.name_ne'
        db.alter_column(u'core_budget', 'name_ne', self.gf('django.db.models.fields.CharField')(default=None, max_length=254))

        # Changing field 'Activity.name_en'
        db.alter_column(u'core_activity', 'name_en', self.gf('django.db.models.fields.CharField')(default=None, max_length=254))

        # Changing field 'Activity.name_ne'
        db.alter_column(u'core_activity', 'name_ne', self.gf('django.db.models.fields.CharField')(default=None, max_length=254))

        # Changing field 'Employee.name_en'
        db.alter_column(u'core_employee', 'name_en', self.gf('django.db.models.fields.CharField')(default=None, max_length=254))

        # Changing field 'Employee.name_ne'
        db.alter_column(u'core_employee', 'name_ne', self.gf('django.db.models.fields.CharField')(default=None, max_length=254))

        # Changing field 'Party.name_ne'
        db.alter_column(u'core_party', 'name_ne', self.gf('django.db.models.fields.CharField')(default=None, max_length=254))

        # Changing field 'Party.name_en'
        db.alter_column(u'core_party', 'name_en', self.gf('django.db.models.fields.CharField')(default=None, max_length=254))

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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'name_ne': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
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