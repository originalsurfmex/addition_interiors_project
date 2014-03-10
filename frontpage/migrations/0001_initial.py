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
            ('title', self.gf('django.db.models.fields.CharField')(default='Addition Interiors', max_length=20)),
        ))
        db.send_create_signal('frontpage', ['Title'])

        # Adding model 'Slider'
        db.create_table('frontpage_slider', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slider_title', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('slider_text', self.gf('django.db.models.fields.TextField')(max_length=200)),
            ('slider_order', self.gf('django.db.models.fields.PositiveSmallIntegerField')(blank=True, default=1, null=True)),
            ('slider_image', self.gf('django.db.models.fields.files.ImageField')(blank=True, max_length=100, null=True)),
        ))
        db.send_create_signal('frontpage', ['Slider'])

        # Adding model 'Marketing'
        db.create_table('frontpage_marketing', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('marketing_title', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('marketing_text', self.gf('django.db.models.fields.TextField')(max_length=300)),
            ('marketing_order', self.gf('django.db.models.fields.PositiveSmallIntegerField')(blank=True, default=1, null=True)),
            ('marketing_image', self.gf('django.db.models.fields.files.ImageField')(blank=True, max_length=100, null=True)),
        ))
        db.send_create_signal('frontpage', ['Marketing'])

        # Adding model 'Feature'
        db.create_table('frontpage_feature', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('feature_title', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('feature_subtitle', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('feature_text', self.gf('django.db.models.fields.TextField')(max_length=300)),
            ('feature_order', self.gf('django.db.models.fields.PositiveSmallIntegerField')(blank=True, default=1, null=True)),
            ('feature_image', self.gf('django.db.models.fields.files.ImageField')(blank=True, max_length=100, null=True)),
        ))
        db.send_create_signal('frontpage', ['Feature'])


    def backwards(self, orm):
        # Deleting model 'Title'
        db.delete_table('frontpage_title')

        # Deleting model 'Slider'
        db.delete_table('frontpage_slider')

        # Deleting model 'Marketing'
        db.delete_table('frontpage_marketing')

        # Deleting model 'Feature'
        db.delete_table('frontpage_feature')


    models = {
        'frontpage.feature': {
            'Meta': {'object_name': 'Feature'},
            'feature_image': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'feature_order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'blank': 'True', 'default': '1', 'null': 'True'}),
            'feature_subtitle': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'feature_text': ('django.db.models.fields.TextField', [], {'max_length': '300'}),
            'feature_title': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'frontpage.marketing': {
            'Meta': {'object_name': 'Marketing'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marketing_image': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'marketing_order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'blank': 'True', 'default': '1', 'null': 'True'}),
            'marketing_text': ('django.db.models.fields.TextField', [], {'max_length': '300'}),
            'marketing_title': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'frontpage.slider': {
            'Meta': {'object_name': 'Slider'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slider_image': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
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