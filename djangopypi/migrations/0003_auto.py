# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Removing M2M table for field owners on 'Package'
        db.delete_table('djangopypi_package_owners')

        # Removing M2M table for field maintainers on 'Package'
        db.delete_table('djangopypi_package_maintainers')

        # Adding M2M table for field group_owner on 'Package'
        db.create_table('djangopypi_package_group_owner', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('package', models.ForeignKey(orm['djangopypi.package'], null=False)),
            ('group', models.ForeignKey(orm['auth.group'], null=False))
        ))
        db.create_unique('djangopypi_package_group_owner', ['package_id', 'group_id'])

        # Adding M2M table for field group_maintainers on 'Package'
        db.create_table('djangopypi_package_group_maintainers', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('package', models.ForeignKey(orm['djangopypi.package'], null=False)),
            ('group', models.ForeignKey(orm['auth.group'], null=False))
        ))
        db.create_unique('djangopypi_package_group_maintainers', ['package_id', 'group_id'])


    def backwards(self, orm):
        
        # Adding M2M table for field owners on 'Package'
        db.create_table('djangopypi_package_owners', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('package', models.ForeignKey(orm['djangopypi.package'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('djangopypi_package_owners', ['package_id', 'user_id'])

        # Adding M2M table for field maintainers on 'Package'
        db.create_table('djangopypi_package_maintainers', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('package', models.ForeignKey(orm['djangopypi.package'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('djangopypi_package_maintainers', ['package_id', 'user_id'])

        # Removing M2M table for field group_owner on 'Package'
        db.delete_table('djangopypi_package_group_owner')

        # Removing M2M table for field group_maintainers on 'Package'
        db.delete_table('djangopypi_package_group_maintainers')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'djangopypi.classifier': {
            'Meta': {'object_name': 'Classifier'},
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True'})
        },
        'djangopypi.distribution': {
            'Meta': {'unique_together': "(('release', 'filetype', 'pyversion'),)", 'object_name': 'Distribution'},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'content': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'filetype': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'md5_digest': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'pyversion': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'release': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'distributions'", 'to': "orm['djangopypi.Release']"}),
            'signature': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'uploader': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'djangopypi.package': {
            'Meta': {'object_name': 'Package'},
            'allow_comments': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'auto_hide': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'group_maintainers': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'packages_maintained'", 'blank': 'True', 'to': "orm['auth.Group']"}),
            'group_owner': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'packages_owned'", 'blank': 'True', 'to': "orm['auth.Group']"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'primary_key': 'True'})
        },
        'djangopypi.release': {
            'Meta': {'unique_together': "(('package', 'version'),)", 'object_name': 'Release'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'hidden': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'metadata_version': ('django.db.models.fields.CharField', [], {'default': "'1.0'", 'max_length': '64'}),
            'package': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'releases'", 'to': "orm['djangopypi.Package']"}),
            'package_info': ('djangopypi.models.PackageInfoField', [], {}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'djangopypi.review': {
            'Meta': {'object_name': 'Review'},
            'comment': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rating': ('django.db.models.fields.PositiveSmallIntegerField', [], {'blank': 'True'}),
            'release': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reviews'", 'to': "orm['djangopypi.Release']"})
        }
    }

    complete_apps = ['djangopypi']
