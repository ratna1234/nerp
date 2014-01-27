# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'AppSettings'
        db.delete_table(u'core_appsettings')

        # Adding model 'AppSetting'
        db.create_table(u'core_appsetting', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('app_name', self.gf('django.db.models.fields.CharField')(max_length=254)),
            ('fiscal_year', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.FiscalYear'])),
            ('header_for_forms', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'core', ['AppSetting'])


    def backwards(self, orm):
        # Adding model 'AppSettings'
        db.create_table(u'core_appsettings', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('app_name', self.gf('django.db.models.fields.CharField')(max_length=254)),
            ('header_for_forms', self.gf('django.db.models.fields.TextField')()),
            ('fiscal_year', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.FiscalYear'])),
        ))
        db.send_create_signal(u'core', ['AppSettings'])

        # Deleting model 'AppSetting'
        db.delete_table(u'core_appsetting')


    models = {
        u'core.appsetting': {
            'Meta': {'object_name': 'AppSetting'},
            'app_name': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'fiscal_year': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.FiscalYear']"}),
            'header_for_forms': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'core.fiscalyear': {
            'Meta': {'object_name': 'FiscalYear'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['core']