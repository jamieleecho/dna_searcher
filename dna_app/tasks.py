from __future__ import absolute_import, unicode_literals
from .models import SequenceModel
from .services import find_seq
from celery import shared_task
from time import sleep
import numpy as np

@shared_task()
def process_seq(seq,entry_id):
    try:
        entry = SequenceModel.objects.get(pk=entry_id)
    except:
        # perhaps retry
        entry = SequenceModel()
        print("Error, no process")
        return
    #sleep(2)
    entry.result = find_seq(seq) #"F in P %d" % np.random.randint(100)
    entry.save()
    return entry.result #"F in P %d" % np.random.randint(100) 
    #return sm.result 
    #sleep(10)
    #return "F in P %d" % np.random.randint(100)
        
@shared_task
def sleepy(dur):
    sleep(dur)
    return 'Done this time'