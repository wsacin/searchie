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
def create_base():
    text = 'hehe hoho'
    value = random.randint(0, 100)

    bases = [Base(text=text, value=i) for i in range(10)]
    Base.objects.bulk_create(bases)
    print("CREATED 10 BASES")

    logs = [Log(num_views=0,
                last_access=datetime.now(tz=UTC))
            for i in range(10)]
    Log.objects.bulk_create(logs)
    print("WITH 10 LOGS")


@periodic_task(
    run_every=timedelta(seconds=10),
    name='add_base',
    ignore_result=True,
)
def add_base():
    name_list =[ request.text for request in requests.get('http://uinames.com/api/') ]


    for i in range(5):
        create_base.delay()

    return "SCHEDULED TASK"
