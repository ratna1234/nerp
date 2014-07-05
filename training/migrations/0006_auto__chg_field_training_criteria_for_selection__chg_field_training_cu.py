# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Training.criteria_for_selection'
        db.alter_column(u'training_training', 'criteria_for_selection', self.gf('froala_editor.fields.FroalaField')(null=True))

        # Changing field 'Training.curriculum'
        db.alter_column(u'training_training', 'curriculum', self.gf('froala_editor.fields.FroalaField')(null=True))

        # Changing field 'Training.objective'
        db.alter_column(u'training_training', 'objective', self.gf('froala_editor.fields.FroalaField')(null=True))

        # Changing field 'Training.output'
        db.alter_column(u'training_training', 'output', self.gf('froala_editor.fields.FroalaField')(null=True))

        # Changing field 'Training.conclusion'
        db.alter_column(u'training_training', 'conclusion', self.gf('froala_editor.fields.FroalaField')(null=True))

        # Changing field 'Training.feedback'
        db.alter_column(u'training_training', 'feedback', self.gf('froala_editor.fields.FroalaField')(null=True))

    def backwards(self, orm):

        # Changing field 'Training.criteria_for_selection'
        db.alter_column(u'training_training', 'criteria_for_selection', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Training.curriculum'
        db.alter_column(u'training_training', 'curriculum', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Training.objective'
        db.alter_column(u'training_training', 'objective', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Training.output'
        db.alter_column(u'training_training', 'output', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Training.conclusion'
        db.alter_column(u'training_training', 'conclusion', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Training.feedback'
        db.alter_column(u'training_training', 'feedback', self.gf('django.db.models.fields.TextField')(null=True))

    models = {
        u'training.category': {
            'Meta': {'object_name': 'Category'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['training.Category']"}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        u'training.file': {
            'Meta': {'object_name': 'File'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'training': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'files'", 'to': u"orm['training.Training']"})
        },
        u'training.organization': {
            'Meta': {'object_name': 'Organization'},
            'address': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone_no': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'training.participant': {
            'Meta': {'object_name': 'Participant'},
            'address': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['training.Organization']", 'null': 'True', 'blank': 'True'}),
            'phone_no': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'training.resourceperson': {
            'Meta': {'object_name': 'ResourcePerson'},
            'address': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['training.Organization']", 'null': 'True', 'blank': 'True'}),
            'phone_no': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'training.targetgroup': {
            'Meta': {'object_name': 'TargetGroup'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['training.TargetGroup']"}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        u'training.training': {
            'Meta': {'object_name': 'Training'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'trainings'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['training.Category']"}),
            'conclusion': ('froala_editor.fields.FroalaField', [], {'null': 'True', 'blank': 'True'}),
            'criteria_for_selection': ('froala_editor.fields.FroalaField', [], {'null': 'True', 'blank': 'True'}),
            'curriculum': ('froala_editor.fields.FroalaField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'ends': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'feedback': ('froala_editor.fields.FroalaField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'objective': ('froala_editor.fields.FroalaField', [], {'null': 'True', 'blank': 'True'}),
            'output': ('froala_editor.fields.FroalaField', [], {'null': 'True', 'blank': 'True'}),
            'participants': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'trainings'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['training.Participant']"}),
            'resource_persons': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'trainings'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['training.ResourcePerson']"}),
            'starts': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'target_groups': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'trainings'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['training.TargetGroup']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '254'})
        }
    }

    complete_apps = ['training']