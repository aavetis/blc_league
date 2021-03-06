# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Match.home_score'
        db.alter_column(u'league_match', 'home_score', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True))

        # Changing field 'Match.away_score'
        db.alter_column(u'league_match', 'away_score', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True))

    def backwards(self, orm):

        # Changing field 'Match.home_score'
        db.alter_column(u'league_match', 'home_score', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=''))

        # Changing field 'Match.away_score'
        db.alter_column(u'league_match', 'away_score', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=1))

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
        u'league.match': {
            'Meta': {'object_name': 'Match'},
            'away': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'away_team'", 'to': u"orm['league.Team']"}),
            'away_score': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'home': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'home_team'", 'to': u"orm['league.Team']"}),
            'home_score': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'messages': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['league.MatchMessage']", 'symmetrical': 'False', 'blank': 'True'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'matches'", 'to': u"orm['league.Season']"}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'1'", 'max_length': '1'})
        },
        u'league.matchmessage': {
            'Meta': {'object_name': 'MatchMessage'},
            'datetime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'sent_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'league.player': {
            'Meta': {'object_name': 'Player'},
            'bio': ('django.db.models.fields.TextField', [], {'max_length': '256', 'blank': 'True'}),
            'blc_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'fav_champ': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'league.season': {
            'Meta': {'object_name': 'Season'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {'max_length': '2000', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'P'", 'max_length': '1'}),
            'teams': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'teamlist'", 'symmetrical': 'False', 'to': u"orm['league.Team']"})
        },
        u'league.squad': {
            'Meta': {'object_name': 'Squad'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['league.Player']"}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['league.Team']"})
        },
        u'league.team': {
            'Meta': {'object_name': 'Team'},
            'bio': ('django.db.models.fields.TextField', [], {'max_length': '600'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'members': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['league.Player']", 'through': u"orm['league.Squad']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['league']