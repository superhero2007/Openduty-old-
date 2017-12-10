# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'ScheduledNotification.incident'
        db.alter_column('openduty_schedulednotification', 'incident_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['openduty.Incident'], null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'ScheduledNotification.incident'
        raise RuntimeError("Cannot reverse this migration. 'ScheduledNotification.incident' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'ScheduledNotification.incident'
        db.alter_column('openduty_schedulednotification', 'incident_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['openduty.Incident']))

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'notification.schedulednotification': {
            'Meta': {'object_name': 'ScheduledNotification', 'db_table': "'openduty_schedulednotification'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'incident': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['openduty.Incident']", 'null': 'True', 'blank': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'notifier': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'send_at': ('django.db.models.fields.DateTimeField', [], {}),
            'user_to_notify': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'notification.usernotificationmethod': {
            'Meta': {'object_name': 'UserNotificationMethod', 'db_table': "'openduty_usernotificationmethod'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'method': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'position': ('django.db.models.fields.IntegerField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'notification_methods'", 'to': u"orm['auth.User']"})
        },
        u'openduty.incident': {
            'Meta': {'unique_together': "(('service_key', 'incident_key'),)", 'object_name': 'Incident'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'details': ('django.db.models.fields.TextField', [], {}),
            'event_type': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'incident_key': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'occurred_at': ('django.db.models.fields.DateTimeField', [], {}),
            'service_key': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['openduty.Service']"})
        },
        u'openduty.schedulepolicy': {
            'Meta': {'object_name': 'SchedulePolicy'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'repeat_times': ('django.db.models.fields.IntegerField', [], {})
        },
        u'openduty.service': {
            'Meta': {'object_name': 'Service'},
            'escalate_after': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('uuidfield.fields.UUIDField', [], {'unique': 'True', 'max_length': '32', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'notifications_disabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'policy': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['openduty.SchedulePolicy']", 'null': 'True', 'blank': 'True'}),
            'retry': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['notification']