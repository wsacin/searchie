from django.db import models


class Base(models.Model):
    value = models.IntegerField()
    text = models.TextField()

    def __unicode__(self):
        return self.value


class Log(models.Model):
    name = models.TextField()
    num_views = models.IntegerField()
    last_access = models.DateTimeField()

    def __unicode__(self):
        return self.name