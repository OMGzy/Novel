# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Chapter(models.Model):
    chapterid = models.AutoField(primary_key=True)
    novelid = models.ForeignKey('Novel', models.DO_NOTHING, db_column='novelid')
    title = models.CharField(max_length=100)
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 'chapter'


class ChapterCopy(models.Model):
    chapterid = models.AutoField(primary_key=True)
    novelid = models.ForeignKey('NovelCopy', models.DO_NOTHING, db_column='novelid')
    title = models.CharField(max_length=100)
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 'chapter_copy'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Novel(models.Model):
    novelid = models.AutoField(primary_key=True)
    type = models.IntegerField()
    novelname = models.CharField(max_length=100)
    novelimg = models.CharField(max_length=100)
    description = models.TextField()
    state = models.CharField(max_length=20)
    author = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'novel'


class NovelCopy(models.Model):
    novelid = models.AutoField(primary_key=True)
    type = models.IntegerField()
    novelname = models.CharField(max_length=100)
    novelimg = models.CharField(max_length=100)
    description = models.TextField()
    state = models.CharField(max_length=20)
    author = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'novel_copy'
