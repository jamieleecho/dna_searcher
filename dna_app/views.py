from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import SeqenceForm
from .models import SequenceModel
from .services import find_seq
from .tasks import process_seq

NUM_SEARCH_HISTORY = 20
# Create your views here.

def home_view(request):
    #return clear_data()  #uncomment to delete prior searches then recomment!
    form = SeqenceForm(request.POST or None)
    
    if form.is_valid():
        seq = ''.join(form.cleaned_data['seq'].upper().split()) #remove newlines and spaces
        form.seq = seq

        form_instance = form.save()
        process_seq.delay(seq,form_instance.id)
        form = SeqenceForm()
        return HttpResponseRedirect('/')
        
    
    searches = SequenceModel.objects.all()[::-1][:NUM_SEARCH_HISTORY]   
    args = {'form':form, 'searches':searches}    
    return render(request, 'home.html',  args)

def home_iframe(request):
    searches = SequenceModel.objects.all()[::-1][:NUM_SEARCH_HISTORY]    
    args = {'searches':searches}    
    return render(request, 'iframe.html',  args)

def clear_data():
    SequenceModel.objects.all().delete()
    return HttpResponse('Deleted Data') 