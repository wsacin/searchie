from datetime import datetime

from django.db.models.signals import post_save, post_delete
from django.core.signals import Signal
from django.dispatch import receiver
from django.conf import settings
from pytz import UTC

from .models import Base, Log
import os.path


# signal for update base doc visualization
visualized_base = Signal(providing_args=["instance"])


@receiver(visualized_base, sender=Base)
def handle_visualized_base(sender, **kwargs):
    instance = kwargs['instance']
    log = Log.objects.get(pk=instance.id)
    log.last_access = datetime.now(tz=UTC)

    log.history += '[' + log.last_access.isoformat() + ']'
    log.history += ' VISUALIZED\n'
    print('History: \n' + log.history)
    log.save()


@receiver(post_save, sender=Base)
def model_post_save(sender, **kwargs):
    instance = kwargs['instance']

    if kwargs['created']:
        log = Log(base=instance,
                  num_views=0,
                  last_access=datetime.now(tz=UTC))
        log.save()
        print('Created: {}'.format(instance.__dict__))
    else:
        print('Saved: {}'.format(instance.__dict__))


@receiver(post_delete, sender=Base)
def model_post_delete(sender, **kwargs):
    print('Deleted: {}'.format(kwargs['instance'].__dict__))


