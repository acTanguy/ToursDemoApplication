# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Person'
        db.create_table(u'goudimel_person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('goudimel', ['Person'])


        # Renaming column for 'Piece.composer_src' to match new field type.
        db.rename_column(u'goudimel_piece', 'composer_src', 'composer_src_id')
        # Changing field 'Piece.composer_src'
        db.alter_column(u'goudimel_piece', 'composer_src_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['goudimel.Person'], null=True))
        # Adding index on 'Piece', fields ['composer_src']
        db.create_index(u'goudimel_piece', ['composer_src_id'])


    def backwards(self, orm):
        # Removing index on 'Piece', fields ['composer_src']
        db.delete_index(u'goudimel_piece', ['composer_src_id'])

        # Deleting model 'Person'
        db.delete_table(u'goudimel_person')


        # Renaming column for 'Piece.composer_src' to match new field type.
        db.rename_column(u'goudimel_piece', 'composer_src_id', 'composer_src')
        # Changing field 'Piece.composer_src'
        db.alter_column(u'goudimel_piece', 'composer_src', self.gf('django.db.models.fields.CharField')(max_length=64, null=True))

    models = {
        'goudimel.book': {
            'Meta': {'object_name': 'Book'},
            'cesr_id': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num_pages': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'publisher': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'remarks': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'rism_id': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'goudimel.person': {
            'Meta': {'object_name': 'Person'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'goudimel.phrase': {
            'Meta': {'object_name': 'Phrase'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phrase_num': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'phrase_start': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'phrase_stop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'phrase_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'piece_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['goudimel.Piece']"}),
            'rhyme': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'goudimel.piece': {
            'Meta': {'object_name': 'Piece'},
            'book_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['goudimel.Book']"}),
            'composer_src': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['goudimel.Person']", 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'forces': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ms_concordances': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'pdf_link': ('django.db.models.fields.URLField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'print_concordances': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['goudimel']