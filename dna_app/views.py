from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import SeqenceForm
from .models import SequenceModel
from .services import find_seq #SearchDNA, 

from .tasks import process_seq, sleepy

from django_celery_results.models import TaskResult

NUM_SEARCH_HISTORY = 20
# Create your views here.

def home_view(request):
    """sleepy.delay(10)
    tasks = TaskResult.objects.all()
    print(tasks)
    return HttpResponse('Done')"""
    form = SeqenceForm(request.POST or None)
    search_result = ''
    
    tasks = TaskResult.objects.all()
    #print(tasks[22].result)
    #print(process_seq.AsyncResult('f75e15f0-bea2-443a-becf-99d053faa598').status)
    
    if form.is_valid():
        seq = ''.join(form.cleaned_data['seq'].upper().split()) #remove newlines and spaces
        print(seq)
        form.seq = seq

        form_instance = form.save()
        process_seq.delay(seq,form_instance.id)
        #print(task_id)
        form = SeqenceForm()
        return HttpResponseRedirect('/')
        
    
    searches = SequenceModel.objects.all()[::-1][:NUM_SEARCH_HISTORY]
    
    args = {'form':form, 'result':search_result, 'searches':searches}
    
    return render(request, 'home.html',  args)