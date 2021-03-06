# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'ProductTranslation.slug'
        db.alter_column(u'products_product_translation', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=128))
        # Adding index on 'ProductTranslation', fields ['slug']
        db.create_index(u'products_product_translation', ['slug'])


    def backwards(self, orm):
        # Removing index on 'ProductTranslation', fields ['slug']
        db.delete_index(u'products_product_translation', ['slug'])


        # Changing field 'ProductTranslation.slug'
        db.alter_column(u'products_product_translation', 'slug', self.gf('django.db.models.fields.CharField')(max_length=128))

    models = {
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        u'products.product': {
            'Meta': {'object_name': 'Product'},
            'code': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '16'}),
            'description': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '10', 'decimal_places': '2'})
        },
        u'products.producttranslation': {
            'Meta': {'unique_together': "[(u'language_code', u'master')]", 'object_name': 'ProductTranslation', 'db_table': "u'products_product_translation'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            u'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['products.Product']"}),
            'name': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '128'}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "u''", 'max_length': '128'})
        }
    }

    complete_apps = ['products']