# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Brand'
        db.create_table('frontpage_brand', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('brand_title', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('brand_image', self.gf('filebrowser.fields.FileBrowseField')(blank=True, max_length=200, null=True)),
        ))
        db.send_create_signal('frontpage', ['Brand'])

        # Adding model 'Relationship'
        db.create_table('frontpage_relationship', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('relationship_title', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('relationship_comment', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('relationshop_image', self.gf('filebrowser.fields.FileBrowseField')(blank=True, max_length=200, null=True)),
        ))
        db.send_create_signal('frontpage', ['Relationship'])


    def backwards(self, orm):
        # Deleting model 'Brand'
        db.delete_table('frontpage_brand')

        # Deleting model 'Relationship'
        db.delete_table('frontpage_relationship')


    models = {
        'frontpage.brand': {
            'Meta': {'object_name': 'Brand'},
            'brand_image': ('filebrowser.fields.FileBrowseField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'brand_title': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'frontpage.feature': {
            'Meta': {'object_name': 'Feature'},
            'feature_image': ('filebrowser.fields.FileBrowseField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'feature_order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'blank': 'True', 'default': '1', 'null': 'True'}),
            'feature_subtitle': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'feature_text': ('django.db.models.fields.TextField', [], {'max_length': '300'}),
            'feature_title': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'frontpage.marketing': {
            'Meta': {'object_name': 'Marketing'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marketing_image': ('filebrowser.fields.FileBrowseField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'marketing_order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'blank': 'True', 'default': '1', 'null': 'True'}),
            'marketing_text': ('django.db.models.fields.TextField', [], {'max_length': '300'}),
            'marketing_title': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'frontpage.relationship': {
            'Meta': {'object_name': 'Relationship'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'relationship_comment': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'relationship_title': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'relationshop_image': ('filebrowser.fields.FileBrowseField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'})
        },
        'frontpage.slider': {
            'Meta': {'object_name': 'Slider'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slider_image': ('filebrowser.fields.FileBrowseField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'slider_order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'blank': 'True', 'default': '1', 'null': 'True'}),
            'slider_text': ('django.db.models.fields.TextField', [], {'max_length': '200'}),
            'slider_title': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'frontpage.title': {
            'Meta': {'object_name': 'Title'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'Addition Interiors'", 'max_length': '20'})
        }
    }

    complete_apps = ['frontpage']