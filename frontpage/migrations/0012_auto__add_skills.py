# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Skills'
        db.create_table('frontpage_skills', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('skills', self.gf('django.db.models.fields.TextField')(max_length=300)),
            ('skills_order', self.gf('django.db.models.fields.PositiveSmallIntegerField')(blank=True, null=True, default=1)),
        ))
        db.send_create_signal('frontpage', ['Skills'])


    def backwards(self, orm):
        # Deleting model 'Skills'
        db.delete_table('frontpage_skills')


    models = {
        'frontpage.about': {
            'Meta': {'object_name': 'About'},
            'about_image': ('filebrowser.fields.FileBrowseField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'}),
            'about_story': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'about_title': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'frontpage.brand': {
            'Meta': {'object_name': 'Brand'},
            'brand_image': ('filebrowser.fields.FileBrowseField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'}),
            'brand_title': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'frontpage.feature': {
            'Meta': {'object_name': 'Feature'},
            'feature_image': ('filebrowser.fields.FileBrowseField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'}),
            'feature_order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'blank': 'True', 'null': 'True', 'default': '1'}),
            'feature_subtitle': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'feature_text': ('django.db.models.fields.TextField', [], {'max_length': '300'}),
            'feature_title': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'frontpage.marketing': {
            'Meta': {'object_name': 'Marketing'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marketing_image': ('filebrowser.fields.FileBrowseField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'}),
            'marketing_order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'blank': 'True', 'null': 'True', 'default': '1'}),
            'marketing_text': ('django.db.models.fields.TextField', [], {'max_length': '300'}),
            'marketing_title': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'frontpage.relationship': {
            'Meta': {'object_name': 'Relationship'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'relationship_comment': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'relationship_image': ('filebrowser.fields.FileBrowseField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'}),
            'relationship_title': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'frontpage.skills': {
            'Meta': {'object_name': 'Skills'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'skills': ('django.db.models.fields.TextField', [], {'max_length': '300'}),
            'skills_order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'blank': 'True', 'null': 'True', 'default': '1'})
        },
        'frontpage.slider': {
            'Meta': {'object_name': 'Slider'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slider_image': ('filebrowser.fields.FileBrowseField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'}),
            'slider_order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'blank': 'True', 'null': 'True', 'default': '1'}),
            'slider_text': ('django.db.models.fields.TextField', [], {'max_length': '200'}),
            'slider_title': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'frontpage.title': {
            'Meta': {'object_name': 'Title'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '20', 'default': "'Addition Interiors'"})
        }
    }

    complete_apps = ['frontpage']