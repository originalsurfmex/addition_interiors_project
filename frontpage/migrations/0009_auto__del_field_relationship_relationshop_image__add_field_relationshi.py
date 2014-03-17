# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Relationship.relationshop_image'
        db.delete_column('frontpage_relationship', 'relationshop_image')

        # Adding field 'Relationship.relationship_image'
        db.add_column('frontpage_relationship', 'relationship_image',
                      self.gf('filebrowser.fields.FileBrowseField')(null=True, blank=True, max_length=200),
                      keep_default=False)

        # Adding field 'About.about_story'
        db.add_column('frontpage_about', 'about_story',
                      self.gf('django.db.models.fields.CharField')(null=True, max_length=1000),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Relationship.relationshop_image'
        db.add_column('frontpage_relationship', 'relationshop_image',
                      self.gf('filebrowser.fields.FileBrowseField')(null=True, blank=True, max_length=200),
                      keep_default=False)

        # Deleting field 'Relationship.relationship_image'
        db.delete_column('frontpage_relationship', 'relationship_image')

        # Deleting field 'About.about_story'
        db.delete_column('frontpage_about', 'about_story')


    models = {
        'frontpage.about': {
            'Meta': {'object_name': 'About'},
            'about_image': ('filebrowser.fields.FileBrowseField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'}),
            'about_story': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '1000'}),
            'about_title': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'frontpage.brand': {
            'Meta': {'object_name': 'Brand'},
            'brand_image': ('filebrowser.fields.FileBrowseField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'}),
            'brand_title': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'frontpage.feature': {
            'Meta': {'object_name': 'Feature'},
            'feature_image': ('filebrowser.fields.FileBrowseField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'}),
            'feature_order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True', 'default': '1'}),
            'feature_subtitle': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'feature_text': ('django.db.models.fields.TextField', [], {'max_length': '300'}),
            'feature_title': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'frontpage.marketing': {
            'Meta': {'object_name': 'Marketing'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marketing_image': ('filebrowser.fields.FileBrowseField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'}),
            'marketing_order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True', 'default': '1'}),
            'marketing_text': ('django.db.models.fields.TextField', [], {'max_length': '300'}),
            'marketing_title': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'frontpage.relationship': {
            'Meta': {'object_name': 'Relationship'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'relationship_comment': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'relationship_image': ('filebrowser.fields.FileBrowseField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'}),
            'relationship_title': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'frontpage.slider': {
            'Meta': {'object_name': 'Slider'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slider_image': ('filebrowser.fields.FileBrowseField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'}),
            'slider_order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True', 'default': '1'}),
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