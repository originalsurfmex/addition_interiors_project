# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Title'
        db.create_table('frontpage_title', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=20, default='Addition Interiors')),
        ))
        db.send_create_signal('frontpage', ['Title'])

        # Adding model 'Slider'
        db.create_table('frontpage_slider', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slider_title', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('slider_text', self.gf('django.db.models.fields.TextField')(max_length=200)),
            ('slider_order', self.gf('django.db.models.fields.PositiveSmallIntegerField')(blank=True, null=True, default=1)),
            ('slider_image', self.gf('filebrowser.fields.FileBrowseField')(blank=True, max_length=200, null=True)),
        ))
        db.send_create_signal('frontpage', ['Slider'])

        # Adding model 'Marketing'
        db.create_table('frontpage_marketing', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('marketing_title', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('marketing_text', self.gf('django.db.models.fields.TextField')(max_length=300)),
            ('marketing_order', self.gf('django.db.models.fields.PositiveSmallIntegerField')(blank=True, null=True, default=1)),
            ('marketing_image', self.gf('filebrowser.fields.FileBrowseField')(blank=True, max_length=200, null=True)),
        ))
        db.send_create_signal('frontpage', ['Marketing'])

        # Adding model 'Feature'
        db.create_table('frontpage_feature', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('feature_title', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('feature_subtitle', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('feature_text', self.gf('django.db.models.fields.TextField')(max_length=300)),
            ('feature_order', self.gf('django.db.models.fields.PositiveSmallIntegerField')(blank=True, null=True, default=1)),
            ('feature_image', self.gf('filebrowser.fields.FileBrowseField')(blank=True, max_length=200, null=True)),
        ))
        db.send_create_signal('frontpage', ['Feature'])

        # Adding model 'Relationship'
        db.create_table('frontpage_relationship', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('relationship_title', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('relationship_comment', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('relationship_image', self.gf('filebrowser.fields.FileBrowseField')(blank=True, max_length=200, null=True)),
        ))
        db.send_create_signal('frontpage', ['Relationship'])

        # Adding model 'Skills'
        db.create_table('frontpage_skills', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('skills', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('skills_order', self.gf('django.db.models.fields.PositiveSmallIntegerField')(blank=True, null=True, default=1)),
        ))
        db.send_create_signal('frontpage', ['Skills'])

        # Adding model 'Brand'
        db.create_table('frontpage_brand', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('brand_title', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('brand_image', self.gf('filebrowser.fields.FileBrowseField')(blank=True, max_length=200, null=True)),
        ))
        db.send_create_signal('frontpage', ['Brand'])

        # Adding model 'About'
        db.create_table('frontpage_about', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('about_title', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('about_story', self.gf('django.db.models.fields.TextField')(max_length=1000)),
            ('about_image', self.gf('filebrowser.fields.FileBrowseField')(blank=True, max_length=200, null=True)),
        ))
        db.send_create_signal('frontpage', ['About'])

        # Adding model 'Services'
        db.create_table('frontpage_services', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('service_title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('service', self.gf('django.db.models.fields.TextField')(max_length=400)),
        ))
        db.send_create_signal('frontpage', ['Services'])


    def backwards(self, orm):
        # Deleting model 'Title'
        db.delete_table('frontpage_title')

        # Deleting model 'Slider'
        db.delete_table('frontpage_slider')

        # Deleting model 'Marketing'
        db.delete_table('frontpage_marketing')

        # Deleting model 'Feature'
        db.delete_table('frontpage_feature')

        # Deleting model 'Relationship'
        db.delete_table('frontpage_relationship')

        # Deleting model 'Skills'
        db.delete_table('frontpage_skills')

        # Deleting model 'Brand'
        db.delete_table('frontpage_brand')

        # Deleting model 'About'
        db.delete_table('frontpage_about')

        # Deleting model 'Services'
        db.delete_table('frontpage_services')


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
            'feature_order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'blank': 'True', 'null': 'True', 'default': '1'}),
            'feature_subtitle': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'feature_text': ('django.db.models.fields.TextField', [], {'max_length': '300'}),
            'feature_title': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'frontpage.marketing': {
            'Meta': {'object_name': 'Marketing'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marketing_image': ('filebrowser.fields.FileBrowseField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'marketing_order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'blank': 'True', 'null': 'True', 'default': '1'}),
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
            'skills_order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'blank': 'True', 'null': 'True', 'default': '1'})
        },
        'frontpage.slider': {
            'Meta': {'object_name': 'Slider'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slider_image': ('filebrowser.fields.FileBrowseField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
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