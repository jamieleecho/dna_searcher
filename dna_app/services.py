from django import forms
from django.http import HttpResponse
#from service_objects.services import Service

from Bio import SeqIO
from Bio import Entrez
Entrez.email = "sasm@stanford.edu"
PROTEINS = ['NC_027867', 'NC_000852', 'NC_007346', 'NC_008724', 'NC_009899', 'NC_014637', 
            'NC_020104', 'NC_023423', 'NC_023640', 'NC_023719']

def find_seq(seq):
        return "Sequence found in NC_027867 at location 42234"
        for protein in PROTEINS:
            handle = Entrez.efetch(db="nucleotide", id=protein, rettype="gb", retmode="text")
            record = SeqIO.read(handle, "genbank")
            handle.close()
            loc = record.seq.find(seq) 
            if loc >= 0:
                return 'Sequence found in %s at location %d' % (protein,loc)
        return 'No sequence found'  

"""class SearchDNA(Service):
    seq = forms.CharField(widget=forms.Textarea, label='DNA Sequence') 
    
    def process(self):
        self.seq = self.cleaned_data['seq']
        #print(self.seq)
        return self.seq
    
    def post_process(self):
        print(find_seq(self.seq))
        return """