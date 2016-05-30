from django.db import models


class Base(models.Model):
    value = models.IntegerField()
    text = models.TextField()

    def __unicode__(self):
        return self.text


class Log(models.Model):
    operation = models.CharField(max_length=20)
    timestamp = models.DateTimeField()
    text = models.TextField()

    def __unicode__(self):
        return self.text
