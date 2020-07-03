from django.db import models
from .services import find_seq 
  
MAX_SEQ_SAVE_LEN = 50
import random

# Create your models here.
class SequenceModel(models.Model):
    seq = models.TextField()
    result = models.TextField(default=' <still searching... >')
    time = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        self.clean_input()
        super().save(*args, **kwargs)

    def clean_input(self):
        if len(self.seq) > MAX_SEQ_SAVE_LEN:
            self.seq = self.seq[:MAX_SEQ_SAVE_LEN] + '...'
        self.seq = ''.join(self.seq.split())