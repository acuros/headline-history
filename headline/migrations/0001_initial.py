# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Press'
        db.create_table(u'headline_press', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'headline', ['Press'])

        # Adding model 'Headline'
        db.create_table(u'headline_headline', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('press', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['headline.Press'])),
            ('title', self.gf('django.db.models.fields.TextField')()),
            ('link', self.gf('django.db.models.fields.TextField')()),
            ('crawled_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'headline', ['Headline'])

        # Adding model 'CrawlLog'
        db.create_table(u'headline_crawllog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('crawled_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'headline', ['CrawlLog'])

        # Adding M2M table for field updated_presses on 'CrawlLog'
        m2m_table_name = db.shorten_name(u'headline_crawllog_updated_presses')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('crawllog', models.ForeignKey(orm[u'headline.crawllog'], null=False)),
            ('press', models.ForeignKey(orm[u'headline.press'], null=False))
        ))
        db.create_unique(m2m_table_name, ['crawllog_id', 'press_id'])


    def backwards(self, orm):
        # Deleting model 'Press'
        db.delete_table(u'headline_press')

        # Deleting model 'Headline'
        db.delete_table(u'headline_headline')

        # Deleting model 'CrawlLog'
        db.delete_table(u'headline_crawllog')

        # Removing M2M table for field updated_presses on 'CrawlLog'
        db.delete_table(db.shorten_name(u'headline_crawllog_updated_presses'))


    models = {
        u'headline.crawllog': {
            'Meta': {'object_name': 'CrawlLog'},
            'crawled_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'updated_presses': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['headline.Press']", 'symmetrical': 'False'})
        },
        u'headline.headline': {
            'Meta': {'object_name': 'Headline'},
            'crawled_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.TextField', [], {}),
            'press': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['headline.Press']"}),
            'title': ('django.db.models.fields.TextField', [], {})
        },
        u'headline.press': {
            'Meta': {'object_name': 'Press'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['headline']