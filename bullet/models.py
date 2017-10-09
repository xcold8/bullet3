# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models
AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')
# Create your models here.
class Base(models.Model):
	created_ts = models.DateTimeField()
	updated_ts = models.DateTimeField().auto_now
	is_active = models.BooleanField()

class Task(Base, models.Model):
	title = models.CharField(max_length=50)
	creator = models.ForeignKey(AUTH_USER_MODEL)
	assignees = [models.ForeignKey(AUTH_USER_MODEL)]
	status = models.CharField(max_length=15)
	tasktype = models.CharField(max_length=15)
	comments = [models.ForeignKey('Comment')]

class Comment(Base, models.Model):
	creator = models.ForeignKey(AUTH_USER_MODEL)
	title = models.TextField(max_length=255)
