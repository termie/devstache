from django.db import models


class Result(models.Model):
  suite = models.CharField(max_length=255)
  arch = models.ForeignKey('Arch')
  result = models.CharField(max_length=16,
                            choices=(('pass', 'pass'),
                                     ('fail', 'fail'),
                                     ('skip', 'skip')))
  version = models.ForeignKey('Version')
  run = models.CharField(max_length=32)
  created_at = models.DateTimeField()


class Arch(models.Model):
  name = models.CharField(max_length=64)
  jenkins_id = models.CharField(max_length=255)


class Version(models.Model):
  name = models.CharField(max_length=64, blank=True, null=True)
  config = models.TextField()

