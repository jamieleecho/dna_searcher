from __future__ import absolute_import, unicode_literals
from .models import SequenceModel
from .services import find_seq
from celery import shared_task

@shared_task()
def process_seq(seq,entry_id):
    try:
        entry = SequenceModel.objects.get(pk=entry_id)
    except:
        # perhaps retry
        entry = SequenceModel()
        print("Error, no process")
        return

    entry.result = find_seq(seq) 
    entry.save()
    return entry.result 
