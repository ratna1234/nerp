# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FiscalYear'
        db.create_table(u'core_fiscalyear', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'core', ['FiscalYear'])


    def backwards(self, orm):
        # Deleting model 'FiscalYear'
        db.delete_table(u'core_fiscalyear')


    models = {
        u'core.fiscalyear': {
            'Meta': {'object_name': 'FiscalYear'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['core']