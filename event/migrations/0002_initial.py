# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Event'
        db.create_table(u'event_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('venue', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['misc.Venue'], unique=True)),
            ('start_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('duration', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('small_picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('attachements', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('end_note', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('special_notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('ended', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('cropping', self.gf(u'django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'event', ['Event'])

        # Adding M2M table for field year_elligible on 'Event'
        m2m_table_name = db.shorten_name(u'event_event_year_elligible')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('event', models.ForeignKey(orm[u'event.event'], null=False)),
            ('year', models.ForeignKey(orm[u'misc.year'], null=False))
        ))
        db.create_unique(m2m_table_name, ['event_id', 'year_id'])

        # Adding M2M table for field dept_elligible on 'Event'
        m2m_table_name = db.shorten_name(u'event_event_dept_elligible')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('event', models.ForeignKey(orm[u'event.event'], null=False)),
            ('department', models.ForeignKey(orm[u'misc.department'], null=False))
        ))
        db.create_unique(m2m_table_name, ['event_id', 'department_id'])

        # Adding M2M table for field hostel_elligible on 'Event'
        m2m_table_name = db.shorten_name(u'event_event_hostel_elligible')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('event', models.ForeignKey(orm[u'event.event'], null=False)),
            ('hostel', models.ForeignKey(orm[u'misc.hostel'], null=False))
        ))
        db.create_unique(m2m_table_name, ['event_id', 'hostel_id'])

        # Adding M2M table for field conducted_by on 'Event'
        m2m_table_name = db.shorten_name(u'event_event_conducted_by')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('event', models.ForeignKey(orm[u'event.event'], null=False)),
            ('club', models.ForeignKey(orm[u'misc.club'], null=False))
        ))
        db.create_unique(m2m_table_name, ['event_id', 'club_id'])

        # Adding model 'TeamEvent'
        db.create_table(u'event_teamevent', (
            (u'event_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['event.Event'], unique=True, primary_key=True)),
            ('deadline_to_register', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('team_size', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('submission', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('submission_on', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('other_notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'event', ['TeamEvent'])

        # Adding model 'IndividualEvent'
        db.create_table(u'event_individualevent', (
            (u'event_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['event.Event'], unique=True, primary_key=True)),
            ('deadline_to_register', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('submission', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('submission_on', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('other_notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'event', ['IndividualEvent'])

        # Adding model 'Lecture'
        db.create_table(u'event_lecture', (
            (u'event_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['event.Event'], unique=True, primary_key=True)),
            ('deadline_to_register', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('lecture_by', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('topic', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('other_notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'event', ['Lecture'])

        # Adding model 'Workshop'
        db.create_table(u'event_workshop', (
            (u'event_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['event.Event'], unique=True, primary_key=True)),
            ('deadline_to_register', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('workshop_on', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('other_notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'event', ['Workshop'])

        # Adding model 'OtherEvent'
        db.create_table(u'event_otherevent', (
            (u'event_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['event.Event'], unique=True, primary_key=True)),
            ('other_notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'event', ['OtherEvent'])


    def backwards(self, orm):
        # Deleting model 'Event'
        db.delete_table(u'event_event')

        # Removing M2M table for field year_elligible on 'Event'
        db.delete_table(db.shorten_name(u'event_event_year_elligible'))

        # Removing M2M table for field dept_elligible on 'Event'
        db.delete_table(db.shorten_name(u'event_event_dept_elligible'))

        # Removing M2M table for field hostel_elligible on 'Event'
        db.delete_table(db.shorten_name(u'event_event_hostel_elligible'))

        # Removing M2M table for field conducted_by on 'Event'
        db.delete_table(db.shorten_name(u'event_event_conducted_by'))

        # Deleting model 'TeamEvent'
        db.delete_table(u'event_teamevent')

        # Deleting model 'IndividualEvent'
        db.delete_table(u'event_individualevent')

        # Deleting model 'Lecture'
        db.delete_table(u'event_lecture')

        # Deleting model 'Workshop'
        db.delete_table(u'event_workshop')

        # Deleting model 'OtherEvent'
        db.delete_table(u'event_otherevent')


    models = {
        u'event.event': {
            'Meta': {'object_name': 'Event'},
            'attachements': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'conducted_by': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['misc.Club']", 'symmetrical': 'False'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'cropping': (u'django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'dept_elligible': ('django.db.models.fields.related.ManyToManyField', [], {'default': '[<Department: Computer Science and Engineering>, <Department: Electrical Engineering>, <Department: Aerospace engineering>, <Department: Biosciences and Bioengineering>, <Department: Chemical Engineering>, <Department: Chemistry>, <Department: Earth sciences>, <Department: Energy sciences>, <Department: Humanities and social science>, <Department: Industrial Design center>, <Department: Physics>, <Department: Metallurigical engineering>, <Department: Other>, <Department: Mechanical engineering>, <Department: Civil Engineering>]', 'to': u"orm['misc.Department']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'duration': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'end_note': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'ended': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hostel_elligible': ('django.db.models.fields.related.ManyToManyField', [], {'default': '[<Hostel: Hostel 1>, <Hostel: Hostel 2>, <Hostel: Hostel 3>, <Hostel: Hostel 4>, <Hostel: Hostel 5>, <Hostel: Hostel 6>, <Hostel: Hostel 7>, <Hostel: Hostel 8>, <Hostel: Hostel 9>, <Hostel: Hostel 10>, <Hostel: Hostel 11>, <Hostel: Hostel 12>, <Hostel: Hostel 13>, <Hostel: Hostel 14>, <Hostel: Hostel 15>]', 'to': u"orm['misc.Hostel']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'small_picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'special_notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'venue': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['misc.Venue']", 'unique': 'True'}),
            'year_elligible': ('django.db.models.fields.related.ManyToManyField', [], {'default': '[<Year: First Year>, <Year: Second Year>, <Year: Third Year>, <Year: Fourth Year>, <Year: Dual Degree>, <Year: Mtech 1>, <Year: Mtech 2>, <Year: PHD>]', 'to': u"orm['misc.Year']", 'symmetrical': 'False'})
        },
        u'event.individualevent': {
            'Meta': {'object_name': 'IndividualEvent', '_ormbases': [u'event.Event']},
            'deadline_to_register': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'event_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['event.Event']", 'unique': 'True', 'primary_key': 'True'}),
            'other_notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'submission': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'submission_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        u'event.lecture': {
            'Meta': {'object_name': 'Lecture', '_ormbases': [u'event.Event']},
            'deadline_to_register': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'event_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['event.Event']", 'unique': 'True', 'primary_key': 'True'}),
            'lecture_by': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'other_notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'topic': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'event.otherevent': {
            'Meta': {'object_name': 'OtherEvent', '_ormbases': [u'event.Event']},
            u'event_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['event.Event']", 'unique': 'True', 'primary_key': 'True'}),
            'other_notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'event.teamevent': {
            'Meta': {'object_name': 'TeamEvent', '_ormbases': [u'event.Event']},
            'deadline_to_register': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'event_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['event.Event']", 'unique': 'True', 'primary_key': 'True'}),
            'other_notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'submission': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'submission_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'team_size': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'})
        },
        u'event.workshop': {
            'Meta': {'object_name': 'Workshop', '_ormbases': [u'event.Event']},
            'deadline_to_register': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'event_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['event.Event']", 'unique': 'True', 'primary_key': 'True'}),
            'other_notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'workshop_on': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'misc.club': {
            'Meta': {'object_name': 'Club'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
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
        u'misc.venue': {
            'Meta': {'object_name': 'Venue'},
            'description': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'misc.year': {
            'Meta': {'object_name': 'Year'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['event']