# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'signup_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=254, db_index=True)),
            ('mobile', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('is_admin', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('department', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['misc.Department'], null=True, blank=True)),
            ('hostel', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['misc.Hostel'], null=True, blank=True)),
            ('year', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['misc.Year'], null=True, blank=True)),
            ('ldap_username', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('rollno', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('alternate_email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('room', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('cropping', self.gf(u'django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'signup', ['User'])

        # Adding M2M table for field skill on 'User'
        m2m_table_name = db.shorten_name(u'signup_user_skill')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'signup.user'], null=False)),
            ('skill', models.ForeignKey(orm[u'misc.skill'], null=False))
        ))
        db.create_unique(m2m_table_name, ['user_id', 'skill_id'])

        # Adding model 'RegistrationCode'
        db.create_table(u'signup_registrationcode', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['signup.User'], unique=True)),
            ('registration_code', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'signup', ['RegistrationCode'])

        # Adding model 'ResetCode'
        db.create_table(u'signup_resetcode', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['signup.User'], unique=True)),
            ('reset_code', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'signup', ['ResetCode'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'signup_user')

        # Removing M2M table for field skill on 'User'
        db.delete_table(db.shorten_name(u'signup_user_skill'))

        # Deleting model 'RegistrationCode'
        db.delete_table(u'signup_registrationcode')

        # Deleting model 'ResetCode'
        db.delete_table(u'signup_resetcode')


    models = {
        u'misc.department': {
            'Meta': {'object_name': 'Department'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'misc.hostel': {
            'Meta': {'object_name': 'Hostel'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'misc.skill': {
            'Meta': {'object_name': 'Skill'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'short_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'misc.year': {
            'Meta': {'object_name': 'Year'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'signup.registrationcode': {
            'Meta': {'object_name': 'RegistrationCode'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'registration_code': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['signup.User']", 'unique': 'True'})
        },
        u'signup.resetcode': {
            'Meta': {'object_name': 'ResetCode'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reset_code': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['signup.User']", 'unique': 'True'})
        },
        u'signup.user': {
            'Meta': {'object_name': 'User'},
            'alternate_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'cropping': (u'django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'department': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['misc.Department']", 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '254', 'db_index': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'hostel': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['misc.Hostel']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'ldap_username': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'rollno': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'room': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'skill': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['misc.Skill']", 'null': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['misc.Year']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['signup']