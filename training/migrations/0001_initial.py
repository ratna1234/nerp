# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'training_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(blank=True, related_name='children', null=True, to=orm['training.Category'])),
            (u'lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal(u'training', ['Category'])

        # Adding model 'TargetGroup'
        db.create_table(u'training_targetgroup', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(blank=True, related_name='children', null=True, to=orm['training.TargetGroup'])),
            (u'lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal(u'training', ['TargetGroup'])

        # Adding model 'Organization'
        db.create_table(u'training_organization', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('address', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'training', ['Organization'])

        # Adding model 'Participant'
        db.create_table(u'training_participant', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('organization', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['training.Organization'], null=True, blank=True)),
            ('address', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('phone_no', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
        ))
        db.send_create_signal(u'training', ['Participant'])

        # Adding model 'ResourcePerson'
        db.create_table(u'training_resourceperson', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('organization', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['training.Organization'], null=True, blank=True)),
            ('address', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('phone_no', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
        ))
        db.send_create_signal(u'training', ['ResourcePerson'])

        # Adding model 'Training'
        db.create_table(u'training_training', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=254)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('starts', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('ends', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('criteria_for_selection', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('objective', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('output', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('conclusion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('feedback', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('curriculum', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'training', ['Training'])

        # Adding M2M table for field categories on 'Training'
        m2m_table_name = db.shorten_name(u'training_training_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('training', models.ForeignKey(orm[u'training.training'], null=False)),
            ('category', models.ForeignKey(orm[u'training.category'], null=False))
        ))
        db.create_unique(m2m_table_name, ['training_id', 'category_id'])

        # Adding M2M table for field target_groups on 'Training'
        m2m_table_name = db.shorten_name(u'training_training_target_groups')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('training', models.ForeignKey(orm[u'training.training'], null=False)),
            ('targetgroup', models.ForeignKey(orm[u'training.targetgroup'], null=False))
        ))
        db.create_unique(m2m_table_name, ['training_id', 'targetgroup_id'])

        # Adding M2M table for field resource_persons on 'Training'
        m2m_table_name = db.shorten_name(u'training_training_resource_persons')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('training', models.ForeignKey(orm[u'training.training'], null=False)),
            ('resourceperson', models.ForeignKey(orm[u'training.resourceperson'], null=False))
        ))
        db.create_unique(m2m_table_name, ['training_id', 'resourceperson_id'])

        # Adding M2M table for field participants on 'Training'
        m2m_table_name = db.shorten_name(u'training_training_participants')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('training', models.ForeignKey(orm[u'training.training'], null=False)),
            ('participant', models.ForeignKey(orm[u'training.participant'], null=False))
        ))
        db.create_unique(m2m_table_name, ['training_id', 'participant_id'])

        # Adding model 'File'
        db.create_table(u'training_file', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=254)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('training', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['training.Training'])),
        ))
        db.send_create_signal(u'training', ['File'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'training_category')

        # Deleting model 'TargetGroup'
        db.delete_table(u'training_targetgroup')

        # Deleting model 'Organization'
        db.delete_table(u'training_organization')

        # Deleting model 'Participant'
        db.delete_table(u'training_participant')

        # Deleting model 'ResourcePerson'
        db.delete_table(u'training_resourceperson')

        # Deleting model 'Training'
        db.delete_table(u'training_training')

        # Removing M2M table for field categories on 'Training'
        db.delete_table(db.shorten_name(u'training_training_categories'))

        # Removing M2M table for field target_groups on 'Training'
        db.delete_table(db.shorten_name(u'training_training_target_groups'))

        # Removing M2M table for field resource_persons on 'Training'
        db.delete_table(db.shorten_name(u'training_training_resource_persons'))

        # Removing M2M table for field participants on 'Training'
        db.delete_table(db.shorten_name(u'training_training_participants'))

        # Deleting model 'File'
        db.delete_table(u'training_file')


    models = {
        u'training.category': {
            'Meta': {'object_name': 'Category'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
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
            'title': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'training': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['training.Training']"})
        },
        u'training.organization': {
            'Meta': {'object_name': 'Organization'},
            'address': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
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
            'conclusion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'criteria_for_selection': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'curriculum': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'ends': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'feedback': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'objective': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'output': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'participants': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'trainings'", 'symmetrical': 'False', 'to': u"orm['training.Participant']"}),
            'resource_persons': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'trainings'", 'symmetrical': 'False', 'to': u"orm['training.ResourcePerson']"}),
            'starts': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'target_groups': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'trainings'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['training.TargetGroup']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '254'})
        }
    }

    complete_apps = ['training']