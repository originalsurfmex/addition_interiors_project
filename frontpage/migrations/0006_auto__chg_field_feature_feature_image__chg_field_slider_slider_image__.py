# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Feature.feature_image'
        db.alter_column('frontpage_feature', 'feature_image', self.gf('filebrowser.fields.FileBrowseField')(max_length=200, null=True))

        # Changing field 'Slider.slider_image'
        db.alter_column('frontpage_slider', 'slider_image', self.gf('filebrowser.fields.FileBrowseField')(max_length=200, null=True))

        # Changing field 'Marketing.marketing_image'
        db.alter_column('frontpage_marketing', 'marketing_image', self.gf('filebrowser.fields.FileBrowseField')(max_length=200, null=True))

    def backwards(self, orm):

        # Changing field 'Feature.feature_image'
        db.alter_column('frontpage_feature', 'feature_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))

        # Changing field 'Slider.slider_image'
        db.alter_column('frontpage_slider', 'slider_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))

        # Changing field 'Marketing.marketing_image'
        db.alter_column('frontpage_marketing', 'marketing_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))

    models = {
        'frontpage.feature': {
            'Meta': {'object_name': 'Feature'},
            'feature_image': ('filebrowser.fields.FileBrowseField', [], {'max_length': '200', 'blank': 'True', 'null': 'True'}),
            'feature_order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'default': '1', 'blank': 'True'}),
            'feature_subtitle': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'feature_text': ('django.db.models.fields.TextField', [], {'max_length': '300'}),
            'feature_title': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'frontpage.marketing': {
            'Meta': {'object_name': 'Marketing'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marketing_image': ('filebrowser.fields.FileBrowseField', [], {'max_length': '200', 'blank': 'True', 'null': 'True'}),
            'marketing_order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'default': '1', 'blank': 'True'}),
            'marketing_text': ('django.db.models.fields.TextField', [], {'max_length': '300'}),
            'marketing_title': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'frontpage.slider': {
            'Meta': {'object_name': 'Slider'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slider_image': ('filebrowser.fields.FileBrowseField', [], {'max_length': '200', 'blank': 'True', 'null': 'True'}),
            'slider_order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'default': '1', 'blank': 'True'}),
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