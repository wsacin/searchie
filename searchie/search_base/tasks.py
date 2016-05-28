from __future__ import absolute_import

import random
import requests

from celery import shared_task
from celery.task import periodic_task
from datetime import timedelta, datetime

from pytz import UTC

from .models import Log, Base


@shared_task
def register_base_deletion(base_id):
    log = Log.objects.get(pk=base_id)
    log.history += '[' + log.last_access.isoformat() + ']'
    log.history += ' BASE DOCUMENT DELETED.\n'
    log.save()
    return log.history


@shared_task
def create_base(json_list):
    bases, logs = [], []
    for person in json_list:
        bases.append(Base(text=(person['name'] + ' ' + person['surname']),
                          value=random.randint(0,100)))
        logs.append(Log(num_views=0,
                    last_access=datetime.now(tz=UTC)))

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
