from django.db import models


class Base(models.Model):
    value = models.IntegerField()
    text = models.TextField()

    def __unicode__(self):
        return self.text


class Log(models.Model):
    num_views = models.IntegerField()
    last_access = models.DateTimeField()
    history = models.TextField()

    def __unicode__(self):
        return 'Log ' + str(self.pk)
