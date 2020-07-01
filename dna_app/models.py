from django.db import models
from .services import find_seq #SearchDNA, 
#from .tasks import process_seq   
MAX_SEQ_SAVE_LEN = 50
import random

# Create your models here.
class SequenceModel(models.Model):
    seq = models.TextField()#blank=True,null=True)
    result = models.TextField(default='<Working on it!>')
    time = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        self.clean_input()
        super().save(*args, **kwargs)

    def clean_input(self):
        if len(self.seq) > MAX_SEQ_SAVE_LEN:
            self.seq = self.seq[:MAX_SEQ_SAVE_LEN] + '...'
        self.seq = ''.join(self.seq.split())
        #self.task_id = process_seq.delay(self.seq,self.task_id)#'Protein A' #'No Sequence Found'        
