# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'About.about_story'
        db.alter_column('frontpage_about', 'about_story', self.gf('django.db.models.fields.TextField')(max_length=1000))

        # Changing field 'Services.service'
        db.alter_column('frontpage_services', 'service', self.gf('django.db.models.fields.TextField')(max_length=400))

    def backwards(self, orm):

        # Changing field 'About.about_story'
        db.alter_column('frontpage_about', 'about_story', self.gf('django.db.models.fields.CharField')(max_length=1000))

        # Changing field 'Services.service'
        db.alter_column('frontpage_services', 'service', self.gf('django.db.models.fields.CharField')(max_length=400))

    models = {
        'frontpage.about': {
            'Meta': {'object_name': 'About'},
            'about_image': ('filebrowser.fields.FileBrowseField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'about_story': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'about_title': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'frontpage.brand': {
            'Meta': {'object_name': 'Brand'},
            'brand_image': ('filebrowser.fields.FileBrowseField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'brand_title': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'frontpage.feature': {
            'Meta': {'object_name': 'Feature'},
            'feature_image': ('filebrowser.fields.FileBrowseField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'feature_order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1', 'blank': 'True', 'null': 'True'}),
            'feature_subtitle': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'feature_text': ('django.db.models.fields.TextField', [], {'max_length': '300'}),
            'feature_title': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'frontpage.marketing': {
            'Meta': {'object_name': 'Marketing'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marketing_image': ('filebrowser.fields.FileBrowseField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'marketing_order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1', 'blank': 'True', 'null': 'True'}),
            'marketing_text': ('django.db.models.fields.TextField', [], {'max_length': '300'}),
            'marketing_title': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'frontpage.relationship': {
            'Meta': {'object_name': 'Relationship'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'relationship_comment': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'relationship_image': ('filebrowser.fields.FileBrowseField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'relationship_title': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'frontpage.services': {
            'Meta': {'object_name': 'Services'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'service': ('django.db.models.fields.TextField', [], {'max_length': '400'}),
            'service_title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'frontpage.skills': {
            'Meta': {'object_name': 'Skills', 'ordering': "['skills_order']"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'skills': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'skills_order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1', 'blank': 'True', 'null': 'True'})
        },
        'frontpage.slider': {
            'Meta': {'object_name': 'Slider'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slider_image': ('filebrowser.fields.FileBrowseField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'slider_order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1', 'blank': 'True', 'null': 'True'}),
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