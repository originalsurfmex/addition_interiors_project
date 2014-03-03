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
            ('slider_order', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, default=1, blank=True)),
        ))
        db.send_create_signal('frontpage', ['Slider'])


    def backwards(self, orm):
        # Deleting model 'Title'
        db.delete_table('frontpage_title')

        # Deleting model 'Slider'
        db.delete_table('frontpage_slider')


    models = {
        'frontpage.slider': {
            'Meta': {'object_name': 'Slider'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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