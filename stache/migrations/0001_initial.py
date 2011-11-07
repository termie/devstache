# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Result'
        db.create_table('stache_result', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('suite', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('arch', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stache.Arch'])),
            ('result', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('version', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stache.Version'])),
            ('run', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('stache', ['Result'])

        # Adding model 'Arch'
        db.create_table('stache_arch', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('jenkins_id', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('stache', ['Arch'])

        # Adding model 'Version'
        db.create_table('stache_version', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('config', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('stache', ['Version'])


    def backwards(self, orm):
        
        # Deleting model 'Result'
        db.delete_table('stache_result')

        # Deleting model 'Arch'
        db.delete_table('stache_arch')

        # Deleting model 'Version'
        db.delete_table('stache_version')


    models = {
        'stache.arch': {
            'Meta': {'object_name': 'Arch'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jenkins_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'stache.result': {
            'Meta': {'object_name': 'Result'},
            'arch': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stache.Arch']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'result': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'run': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'suite': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'version': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stache.Version']"})
        },
        'stache.version': {
            'Meta': {'object_name': 'Version'},
            'config': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['stache']
