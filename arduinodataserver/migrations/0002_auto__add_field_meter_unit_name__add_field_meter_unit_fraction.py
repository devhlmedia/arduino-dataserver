# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Meter.unit_name'
        db.add_column('arduinodataserver_meter', 'unit_name',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Meter.unit_fraction'
        db.add_column('arduinodataserver_meter', 'unit_fraction',
                      self.gf('django.db.models.fields.FloatField')(default=1),
                      keep_default=False)

    def backwards(self, orm):
        # Deleting field 'Meter.unit_name'
        db.delete_column('arduinodataserver_meter', 'unit_name')

        # Deleting field 'Meter.unit_fraction'
        db.delete_column('arduinodataserver_meter', 'unit_fraction')

    models = {
        'arduinodataserver.interval': {
            'Meta': {'unique_together': "(('interval_type', 'from_time'),)", 'object_name': 'Interval'},
            'average': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'data_entries': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'from_time': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interval_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['arduinodataserver.IntervalType']"}),
            'to_time': ('django.db.models.fields.DateTimeField', [], {}),
            'total': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'blank': 'True'})
        },
        'arduinodataserver.intervaltype': {
            'Meta': {'object_name': 'IntervalType'},
            'backlog': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'force_recreate': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meter_set': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['arduinodataserver.Meter']", 'symmetrical': 'False', 'blank': 'True'}),
            'name': ('django.db.models.fields.IntegerField', [], {}),
            'unit_fraction': ('django.db.models.fields.FloatField', [], {'default': '1'}),
            'unit_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'verbose_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'arduinodataserver.meter': {
            'Meta': {'object_name': 'Meter'},
            'default_interval': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'default_meter'", 'null': 'True', 'to': "orm['arduinodataserver.IntervalType']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_counter': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'meter_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['arduinodataserver.MeterType']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'unit_fraction': ('django.db.models.fields.FloatField', [], {'default': '1'}),
            'unit_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'arduinodataserver.meterdata': {
            'Meta': {'object_name': 'MeterData'},
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'data_point': ('django.db.models.fields.FloatField', [], {}),
            'diff': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['arduinodataserver.Meter']"})
        },
        'arduinodataserver.metertype': {
            'Meta': {'object_name': 'MeterType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['arduinodataserver']