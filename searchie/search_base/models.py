from django.db import models
from .tasks import register_base_deletion


class Base(models.Model):
    value = models.IntegerField()
    text = models.TextField()

    def delete(self, using=None, keep_parents=False):
        result = register_base_deletion.apply_async((2,2))
        super(Base, self).delete(using=using,
                                 keep_parents=keep_parents)

    def __unicode__(self):
        return self.text


class Log(models.Model):
    base = models.ForeignKey(Base)
    num_views = models.IntegerField()
    last_access = models.DateTimeField()
    history = models.TextField()

    def __unicode__(self):
        return self.base
