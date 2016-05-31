from datetime import datetime

from django.core.signals import Signal
from django.dispatch import receiver
from pytz import UTC

from .models import Base, Log

# signal for update base doc visualization
visualised_base_signal = Signal(providing_args=["instance"])
updated_base_signal = Signal(providing_args=["instance", "new_data"])


@receiver(visualised_base_signal, sender=Base)
def handle_visualised_base(sender, **kwargs):
    base = kwargs['instance']
    timestamp = datetime.now(tz=UTC)

    log = Log(pk=base.pk,
              operation='visualisation',
              timestamp=timestamp,
              text='[{0}] Base {1} ({2},{3}) visualised.'
                    .format(timestamp, base.pk, base.value, base.text))
    log.save()


@receiver(updated_base_signal, sender=Base)
def handle_updated_base(sender, **kwargs):
    base = kwargs['instance']
    new_data = kwargs['new_data']
    timestamp = datetime.now(tz=UTC)
    text = '[{0}] Base {1} ({2},{3}) was updated to ({4},{5})'\
                .format(timestamp, base.pk,
                        base.value, base.text,
                        new_data['value'], new_data['text'])

    log = Log(pk=base.pk,
              operation='update',
              timestamp=timestamp,
              text=text)
    log.save()

