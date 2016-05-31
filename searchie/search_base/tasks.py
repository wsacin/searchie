from __future__ import absolute_import

import random
import requests

from celery import shared_task
from celery.task import periodic_task
from datetime import timedelta, datetime

from pytz import UTC

from .models import Log, Base


@shared_task
def register_base_deletion(base_id,base_value,base_text):
    timestamp = datetime.now(tz=UTC)
    info = "[{0}] Base document {1} ({2},'{3}') was deleted."\
        .format(timestamp, base_id, base_value, base_text)

    log = Log(pk=base_id,
              operation='deletion',
              timestamp=timestamp,
              text=info)
    log.save()
    return log.text


@shared_task
def create_base(json_list):
    bases, logs = [], []
    for person in json_list:
        value = random.randint(0, 100)
        text = person['name'] + ' ' + person['surname']
        timestamp = datetime.now(tz=UTC)

        base = Base(text=text, value=value)
        log = Log(pk=base.pk,
                  operation='creation',
                  timestamp=timestamp,
                  text='[{0}] Base {1} ({2},{3}) created.'
                        .format(timestamp, base.pk, value, text))

        bases.append(base)
        logs.append(log)

    Base.objects.bulk_create(bases)
    Log.objects.bulk_create(logs)

    return "CREATED 160 BASES WITH 160 LOGS"


@periodic_task(
    run_every=timedelta(seconds=10),
    name='add_base',
    ignore_result=True,
)
def add_base():
    r = requests.get('http://uinames.com/api/?amount=160&region=united states')
    create_base.delay(r.json())

    return "SCHEDULED TASK"
