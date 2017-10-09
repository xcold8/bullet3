# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


TASK_TYPE_BUG = 1
TASK_TYPE_FEATURE = 2
TASK_TYPE_CHORE = 3
TASK_TYPES = [
    (TASK_TYPE_BUG, "Bug"),
    (TASK_TYPE_FEATURE, "Feature"),
    (TASK_TYPE_CHORE, "Chore"),
]


TASK_STATUS_NEW = 1
TASK_STATUS_STARTED = 2
TASK_STATUS_FINISHED = 3
TASK_STATUS_ACCEPTED = 4
TASK_STATUS_REJECTED = 5
TASK_STATUSES = [
    (TASK_STATUS_NEW, "New"),
    (TASK_STATUS_STARTED, "Started"),
    (TASK_STATUS_FINISHED, "Finished"),
    (TASK_STATUS_ACCEPTED, "Accepted"),
    (TASK_STATUS_REJECTED, "Rejected"),
]


# BASE 
class Base(models.Model):
    created_ts = models.DateTimeField(default=datetime.now)
    updated_ts = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


# APP
class Task(Base):
    title = models.CharField(max_length=128, null=False, blank=False)
    creator = models.ForeignKey(User, related_name="created_tasks")
    assignees = models.ManyToManyField(User, related_name="assigned_tasks")
    #status = models.CharField(max_length=15)
    status = models.IntegerField(choices=TASK_STATUSES, default=TASK_STATUS_NEW)
    #tasktype = models.CharField(max_length=15)
    task_type = models.IntegerField(choices=TASK_TYPES, blank=False, null=False)

    class Meta:
        db_table = "task"


class Comment(Base):
    task = models.ForeignKey("Task", related_name="comments")
    creator = models.ForeignKey(User)
    title = models.TextField(max_length=512)

    class Meta:
        db_table = "comment"
